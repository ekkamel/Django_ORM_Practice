from django.db import models
from datetime import date, datetime 

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    LOCATION = [
        ("Heliopolis", "Heliopolis"), 
        ("Nasr City", "Nasr City"), 
        ("Dokki", "Dokki"), 
        ("New Cairo", "New Cairo"), 
        ("New Giza", "New Giza"), 
    ]
    location = models.CharField(max_length=15, default="New Cairo", choices=LOCATION)
    email = models.EmailField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    section = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    reg_date = models.DateField(default=date.today)
        
    def __str__(self):
        return f"({self.name}, {self.school})"