from django.urls import path
from school.models import School, Student
from . import views

urlpatterns = [
    path("students/", views.get_students, name="get_students"),
]