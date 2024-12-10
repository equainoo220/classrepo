from django.db import models

# Create your models here.
class Student(models.Model):
    cnumber = models.CharField(primary_key=True, max_length=10)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    dob = models.DateField()
    gpa = models.FloatField()
    
    def __str__(self):
        return self.lastname
    
    