from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    grade = models.IntegerField(default=0)
    def __str__(self):
        return self.first_name + " " + self.last_name
