from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

class ClassAverage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0)
