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
            "grade": student.grade,  
            "school": student.school.name,            
        })

    data = {
        "students": student_data, 
    }

    return JsonResponse(data, safe=False)


def get_schools(request): 
    schools = School.objects.all()
    
    school_data = []
    for school in schools: 
        school_data.append({
            "name": school.name, 
            "location": school.location, 
        })
        
    data = {
        "schools": school_data
    }
    
    return JsonResponse(data, safe=False)