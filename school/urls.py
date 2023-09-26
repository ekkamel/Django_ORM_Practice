from django.urls import path
from school.models import School, Student
from .views import get_schools, get_students, get_student, get_filter_options, student_grade_chart, statistics_view, cards

urlpatterns = [
    path("statistics/", statistics_view, name="student-statistics"), 
    path("students/", get_students, name="get_students"),
    path("schools/", get_schools, name="get_schools"),
    path("student/<int:student_id>", get_student, name="get_student"), 
    path("grade-chart/<int:year>/", student_grade_chart, name="student-grade-chart"),
    path("filter-options/", get_filter_options, name="chart-filter-options"),  
    path('cards/', cards, name='cards'),   
]