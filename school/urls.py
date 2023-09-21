from django.urls import path
from school.models import School, Student
from .views import get_schools, get_students, get_student

urlpatterns = [
    path("students/", get_students, name="get_students"),
    path("schools/", get_schools, name="get_schools"),
    path("student/<int:student_id>", get_student, name="get_student"), 
]