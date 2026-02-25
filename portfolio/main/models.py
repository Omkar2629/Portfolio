from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    category = models.CharField(max_length=100)  # ⭐ Soft Skills / Tools
    name = models.CharField(max_length=100)      # ⭐ actual skill
    proficiency = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.category} - {self.name}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Internship(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.company


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    score = models.CharField(max_length=50)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.degree

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Certification(models.Model):
    title = models.CharField(max_length=250)
    issuer = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='certifications/', null=True, blank=True)
    credential_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

