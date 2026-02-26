from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
import io

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    internships = Internship.objects.all()
    education = Education.objects.all()
    certifications = Certification.objects.all().order_by('-year')

    return render(request, "home.html", {
        "skills": skills,
        "projects": projects,
        "internships": internships,
        "education": education,
        "certifications": certifications,
    })
from django.shortcuts import render, redirect

def greet(request):
    if request.method == "POST":
        name = request.POST.get("name")
        request.session["visitor_name"] = name
        return redirect("home")

    return render(request, "greet.html")

from .models import Project

def projects_list(request):
    projects = Project.objects.all().order_by('-created_date')
    return render(request, 'projects_list.html', {'projects': projects})
def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'project_detail.html', {'project': project})

from .nlp_utils import summarize_text

# STEP 1 — Show CV Form
def generate_cv(request):
    return render(request, 'cv_form.html')

# STEP 2 — After form submit → store in session → show template selector
def choose_template(request):
    if request.method == 'POST':
        request.session['cv_post_data'] = request.POST
        request.session['cv_files_data'] = request.FILES
        return render(request, 'cv_template_select.html')

    return redirect('generate_cv')


# STEP 3 — Render selected template
def render_selected_cv(request, template_name):
    from django.http import QueryDict

    raw_post_data = request.session.get('cv_post_data')

    if not raw_post_data:
        return redirect('generate_cv')

    post_data = QueryDict('', mutable=True)
    post_data.update(raw_post_data)

    files_data = request.session.get('cv_files_data')

    if not post_data:
        return redirect('generate_cv')

    # 🔥 Get lists
    project_paragraphs = post_data.getlist('projects')
    project_titles = post_data.getlist('project_titles')

    project_data = []

    # 🔥 SMART ADAPTIVE PROCESSING (your logic preserved)
    for title, para in zip(project_titles, project_paragraphs):

        clean_para = (para or "").strip()

        # Case 0: empty
        if not clean_para:
            summary = []

        # Case 1: user typed bullet-style lines
        elif "\n" in clean_para and len(clean_para.split(".")) <= 2:
            summary = [
                line.strip()
                for line in clean_para.split("\n")
                if line.strip()
            ]

        # Case 2: normal paragraph → use NLTK
        else:
            summary = summarize_text(clean_para, num_sentences=3)

        project_data.append({
            "title": (title or "").strip() or "Project",
            "summary": summary
        })

    profile_image = None
    if files_data:
        profile_image = files_data.get('profile_image')

    context = {
        'name': post_data.get('name') or "N/A",
        'email': post_data.get('email') or "N/A",
        'phone': post_data.get('phone') or "N/A",
        'education': post_data.get('education') or "N/A",
        'skills': post_data.get('skills') or "N/A",
        'projects_data': project_data,
        'internships': post_data.get('internships') or "N/A",
        'certifications': post_data.get('certifications') or "N/A",
        'linkedin': post_data.get('linkedin') or "N/A",
        'github': post_data.get('github') or "N/A",
        'profile_image': profile_image,
    }

    template_map = {
        "generalised": "cv_templates/generalised_template.html",
        "modern": "cv_templates/modern_template.html",
        "minimal": "cv_templates/minimal_template.html",
        "dark": "cv_templates/executive_template.html",
    }

    return render(request, template_map[template_name], context)

from .models import ContactMessage
from django.shortcuts import redirect

from django.core.mail import send_mail
from django.conf import settings

def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Email to YOU (admin)
        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        # Auto reply to USER
        send_mail(
            subject="Thanks for contacting Omkar!",
            message="Hi! Thanks for reaching out. I’ll get back to you soon 🙂",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

    return redirect('/home/')

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from .models import Skill, Project, Certification


@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Access Denied")

    skill_count = Skill.objects.count()
    project_count = Project.objects.count()
    cert_count = Certification.objects.count()

    context = {
        "skill_count": skill_count,
        "project_count": project_count,
        "cert_count": cert_count,
    }

    return render(request, "dashboard.html", context)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def manage_skills(request):
    skills = Skill.objects.filter(user=request.user)

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect("manage_skills")
    else:
        form = SkillForm()

    context = {
        "form": form,
        "skills": skills,
    }
    return render(request, "manage_skills.html", context)

@login_required
def manage_projects(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Access Denied")

    projects = Project.objects.all()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_projects')
    else:
        form = ProjectForm()

    return render(request, "manage_projects.html", {
        "projects": projects,
        "form": form
    })


from .models import Skill, Project, Internship, Education, ContactMessage, Certification
from .forms import SkillForm, ProjectForm, InternshipForm, EducationForm

@login_required
def delete_skill(request, skill_id):
    skill = get_object_or_404(
        Skill,
        id=skill_id,
        user=request.user  # 🔥 ownership check
    )

    if request.method == "POST":
        skill.delete()

    return redirect("manage_skills")

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        project.delete()

    return redirect("manage_projects")

from .models import Certification
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


@login_required
def manage_certifications(request):
    certifications = Certification.objects.order_by('-year')

    if request.method == 'POST':
        form = CertificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Certification added successfully.")
            return redirect('manage_certifications')
    else:
        form = CertificationForm()

    return render(request, 'manage_certifications.html', {
        'certifications': certifications,
        'form': form,
    })


@login_required
def delete_certification(request, cert_id):
    cert = get_object_or_404(Certification, id=cert_id)
    cert.delete()
    return redirect('manage_certifications')

from .forms import CertificationForm
from django.contrib import messages


template_map = {
    "classic": "cv_templates/template_classic.html",
    "modern": "cv_templates/template_modern.html",
    "minimal": "cv_templates/template_minimal.html",
    "generalised": "cv_templates/generalised_template.html",
}

def download_cv_pdf(request, template_name):
    from django.http import QueryDict

    raw_post_data = request.session.get('cv_post_data')

    if not raw_post_data:
        return redirect('generate_cv')

    post_data = QueryDict('', mutable=True)
    post_data.update(raw_post_data)

    files_data = request.session.get('cv_files_data')

    # ---------- project processing (same logic) ----------
    project_paragraphs = post_data.getlist('projects')
    project_titles = post_data.getlist('project_titles')

    project_data = []

    for title, para in zip(project_titles, project_paragraphs):
        clean_para = (para or "").strip()

        if not clean_para:
            summary = []
        elif "\n" in clean_para and len(clean_para.split(".")) <= 2:
            summary = [line.strip() for line in clean_para.split("\n") if line.strip()]
        else:
            summary = summarize_text(clean_para, num_sentences=3)

        project_data.append({
            "title": (title or "").strip() or "Project",
            "summary": summary
        })

    profile_image = None
    if files_data:
        profile_image = files_data.get('profile_image')

    context = {
        'name': post_data.get('name') or "N/A",
        'email': post_data.get('email') or "N/A",
        'phone': post_data.get('phone') or "N/A",
        'role': post_data.get('role') or "",
        'summary': post_data.get('summary') or "",
        'education': post_data.get('education') or "N/A",
        'skills': post_data.get('skills') or "N/A",
        'projects_data': project_data,
        'internships': post_data.get('internships') or "N/A",
        'certifications': post_data.get('certifications') or "N/A",
        'linkedin': post_data.get('linkedin') or "N/A",
        'github': post_data.get('github') or "N/A",
        'profile_image': profile_image,
    }

    template_map = {
        "generalised": "cv_templates/generalised_template.html",
        "modern": "cv_templates/modern_template.html",
        "minimal": "cv_templates/minimal_template.html",
        "executive": "cv_templates/executive_template.html",
    }

    template = get_template(template_map[template_name])
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    filename = f"{template_name}_cv.pdf"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), dest=response)

    return response

def edit_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)

    if request.method == 'POST':
        skill.category = request.POST.get('category')
        skill.name = request.POST.get('name')
        skill.proficiency = request.POST.get('proficiency')
        skill.save()
        return redirect('manage_skills')

    return render(request, 'edit_skill.html', {'skill': skill})



