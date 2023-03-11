# from tkinter import CASCADE 
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class University(models.Model):
    id = models.BigAutoField(primary_key=True )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university_name = models.ForeignKey(University,on_delete=models.CASCADE)  
    registration_no = models.IntegerField()
    student_result = models.ImageField(upload_to = 'result')

    def __str__(self):
        return str(self.registration_no)
    
