from django.shortcuts import render
from django.http import HttpResponse

from .models import Student

# Create your views here.
def index(request):
    all_students = Student.objects.all()
    output = ([student.first_name + ' ' + student.last_name + '\n' for student in all_students])
    return HttpResponse(output)
def detail(request, student_first_name, student_last_name):
    return HttpResponse("Student details for %s %s:" %(student_first_name, student_last_name))
def update(request, student_first_name, student_last_name):
    return HttpResponse("Update student details for %s %s:" %(student_first_name, student_last_name))
