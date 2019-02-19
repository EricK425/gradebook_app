from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("All students:")
def detail(request, student_first_name, student_last_name):
    return HttpResponse("Student details for %s %s:" %(student_first_name, student_last_name))
def update(request, student_first_name, student_last_name):
    return HttpResponse("Update student details for %s %s:" %(student_first_name, student_last_name))
