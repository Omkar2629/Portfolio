from django.urls import path
from . import views

urlpatterns = [
    path("", views.greet, name="greet"),
    path('home/',views.home, name='home'),
]
