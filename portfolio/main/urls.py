from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .api_views import (
    project_list_api,
    project_detail_api,
    project_create_api,
    contact_create_api,
)

urlpatterns = [
    path('', views.greet, name="greet"),
    path('home/', views.home, name='home'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('generate-cv/', views.generate_cv, name='generate_cv'),
    path('contact-submit/', views.contact_submit, name='contact_submit'),

    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/skills/', views.manage_skills, name='manage_skills'),
    path('dashboard/projects/', views.manage_projects, name='manage_projects'),
    path('dashboard/skills/delete/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('dashboard/projects/delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('dashboard/certifications/', views.manage_certifications, name='manage_certifications'),
    path('dashboard/certifications/delete/<int:cert_id>/', views.delete_certification, name='delete_certification'),
    path('generate-cv/', views.generate_cv, name='generate_cv'),
    path('choose-template/', views.choose_template, name='choose_template'),
    path('cv/<str:template_name>/', views.render_selected_cv, name='render_selected_cv'),
    path('cv-download/<str:template_name>/', views.download_cv_pdf, name='download_cv_pdf'),
    path('api/projects/', project_list_api),
    path('api/projects/create/', project_create_api),
    path('api/projects/<slug:slug>/', project_detail_api),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
