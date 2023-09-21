from django.shortcuts import render
from django.http import JsonResponse
from school.models import School, Student
from django.shortcuts import render

# Create your views here.
def get_students(request): 
    students = Student.objects.all()
    
    students_data = []
    for student in students: 
        students_data.append({
            "id": student.id,
            "name": student.name, 
            "grade": student.grade,  
            "school": student.school.name,            
        })

    data = {
        "students": students_data, 
    }

    return JsonResponse(data, safe=False)



def get_student(request, student_id): 
    student = Student.objects.get(pk=student_id)
    
    student_data = {
        "id": student.id,
        "name": student.name, 
        "grade": student.grade,  
        "school": student.school.name, 
        "registered": student.reg_date,
    }
    
    return JsonResponse(student_data)    
    


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