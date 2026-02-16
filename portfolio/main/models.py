from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)

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