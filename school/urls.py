from django.urls import path
from school.models import School, Student
from .views import get_students

urlpatterns = [
    path("students/", get_students, name="get_students"),
]