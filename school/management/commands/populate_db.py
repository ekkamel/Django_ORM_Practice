import random
from datetime import datetime, timedelta 
import pytz
from django.core.management.base import BaseCommand, CommandParser
from school.models import School, Student


class Command(BaseCommand): 
    help = "Populate the database with random generated data."
    
    def add_arguments(self, parser): 
        parser.add_argument("--amount", type=int, help="The number of items that should be added")
        
    def handle(self, *args, **options): 
        names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles"]
        surname = ["Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johnson", "Davies", "Patel", "Wright"]
        grade = ["7", "8", "9", "10", "11", "12"]
        section = ["A", "B", "C", "D", "E"]
        schools = [
            School.objects.get_or_create(name="School 1", email="school1@gmail.com"), School.objects.get_or_create(name="School 2", email="school2.yahoo.com"), 
            School.objects.get_or_create(name="School 3", email="school3@gmail.com"), School.objects.get_or_create(name="School 4", email="school4.yahoo.com"),
            School.objects.get_or_create(name="School 5", email="school5@gmail.com"), School.objects.get_or_create(name="School 6", email="school6.yahoo.com"),
            School.objects.get_or_create(name="School 7", email="school7@gmail.com"), School.objects.get_or_create(name="School 8", email="school8.yahoo.com"),
        ]
        amount = options["amount"] if options["amount"] else 2500
        for i in range(0, amount): 
            dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0,1825)))
            student = Student.objects.create(
                name = random.choice(names) + " " + random.choice(surname), 
                grade = random.choice(grade), 
                section = random.choice(section), 
                school = random.choice(schools)[0], 
                #student.School.location = random.choice(School.LOCATION)[0],                                
            ) 
            student.reg_date = dt
            student.save()
        
        self.stdout.write(self.style.SUCCESS("Successfully populated the database")) 