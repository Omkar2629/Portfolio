from .models import Skill, Project, Internship, Education
from django.shortcuts import render

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    internships = Internship.objects.all()
    education = Education.objects.all()

    return render(request, "home.html", {
        "skills": skills,
        "projects": projects,
        "internships": internships,
        "education": education
    })
from django.shortcuts import render, redirect

def greet(request):
    if request.method == "POST":
        name = request.POST.get("name")
        request.session["visitor_name"] = name
        return redirect("home")

    return render(request, "greet.html")