from django.shortcuts import render
from django.http import JsonResponse
from school.models import School, Student
from django.shortcuts import render
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models import Count, F, Sum, Avg

from .utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict

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
            "School_location": student.school.location          
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


# This view populates the Options drop down list
def get_filter_options(request): 
    grouped_registrations = Student.objects.annotate(year=ExtractYear("reg_date")).values("year").order_by("-year").distinct()
    options = [registration["year"] for registration in grouped_registrations]
    
    return JsonResponse({
        "options": options,
    })
    

def student_grade_chart(request, year): 
    grades = Student.objects.filter(reg_date__year=year)
    grouped_grades = grades.values("grade").annotate(count=Count("id"))\
        .values("grade", "count").order_by("grade") 
    
    grade_dict = dict()
    
    #for grade in Student.grade:
    #    grade_dict[grade[1]] = 0 
    
    for group in grouped_grades: 
        grade_dict[dict(Student.grade)[group["grade"]]] = group["count"]
        
    return JsonResponse({
        "title": f"Registered grades in {year}", 
        "data": {
            "labels": list(grade_dict.keys()), 
            "datasets": [{
                "label": "Students", 
                "backgroundColor": generate_color_palette(len(grade_dict)), 
                "borderColor": generate_color_palette(len(grade_dict)), 
                "data": list(grade_dict.values()), 
            }]
        },
    })