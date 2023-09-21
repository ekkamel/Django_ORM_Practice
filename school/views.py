from django.shortcuts import render
from django.http import JsonResponse
from school.models import School, Student
from django.shortcuts import render

# Create your views here.
def get_students(request): 
    students = Student.objects.all()
    
    student_data = []
    for student in students: 
        student_data.append({
            "name": student.name, 
            "grade": student.grade
        })

    data = {
        "students": student_data, 
    }


    return JsonResponse(data, safe=False)

