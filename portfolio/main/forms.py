from django import forms
from .models import Skill, Project, Internship, Education, Certification


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['title', 'issuer', 'year', 'credential_link']
