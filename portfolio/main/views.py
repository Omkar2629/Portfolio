from .models import Skill, Project, Internship, Education
from django.shortcuts import render

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

def generate_cv(request):
    return render(request, 'cv_form.html')

def cv_preview(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'education': request.POST.get('education'),
            'skills': request.POST.get('skills'),
            'projects': request.POST.get('projects'),
            'internships': request.POST.get('internships'),
            'certifications': request.POST.get('certifications'),
            'linkedin': request.POST.get('linkedin'),
            'github': request.POST.get('github'),
        }
        return render(request, 'cv_preview.html', data)

    return redirect('generate_cv')

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


@login_required
def manage_skills(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Access Denied")

    skills = Skill.objects.all()

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_skills')
    else:
        form = SkillForm()

    return render(request, "manage_skills.html", {
        "skills": skills,
        "form": form
    })

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
    if not request.user.is_superuser:
        return HttpResponseForbidden("Access Denied")

    skill = Skill.objects.get(id=skill_id)

    if request.method == "POST":
        skill.delete()
        return redirect('manage_skills')

    return redirect('manage_skills')

@login_required
def delete_project(request, project_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Access Denied")

    project = Project.objects.get(id=project_id)

    if request.method == "POST":
        project.delete()
        return redirect('manage_projects')

    return redirect('manage_projects')

from .models import Certification
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


@login_required
def manage_certifications(request):
    certifications = Certification.objects.all().order_by('-year')
    return render(request, 'manage_certifications.html', {
        'certifications': certifications
    })


@login_required
def delete_certification(request, cert_id):
    cert = get_object_or_404(Certification, id=cert_id)
    cert.delete()
    return redirect('manage_certifications')



