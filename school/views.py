from django.shortcuts import render
from django.http import JsonResponse
from school.models import School, Student

# Create your views here.
def get_students(request): 
    students = Student.objects.all()

    return JsonResponse({
        "students": students,
    })

