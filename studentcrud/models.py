from django.db import models

# Create your models here.

class Student(models.Model):
    DEPARTMENTS = [
        ('ICT', 'ICT'),
        ('CSE', 'CSE'),
        ('TE', 'TE'),
        ('ME', 'ME')
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    cgpa = models.FloatField(null=True)
    department = models.CharField(max_length=50, choices=DEPARTMENTS, default='ICT')

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, age: {self.age}, department: {self.department}"

