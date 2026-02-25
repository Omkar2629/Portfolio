from django import forms
from .models import Skill, Project, Internship, Education, Certification


from django import forms
from .models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['category', 'name', 'proficiency']
        widgets = {
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Soft Skills / Tools'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter skill'
            }),
            'proficiency': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional'
            }),
        }

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
        fields = [
            'title',
            'issuer',
            'year',
            'credential_link',
            'description',
            'image',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'issuer': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'credential_link': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
