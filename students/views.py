from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Student

# Create your views here.
def index(request):
    all_students = Student.objects.order_by('last_name')
    template = loader.get_template('students/index.html')
    context = {
        'all_students': all_students,
    }
    return HttpResponse(template.render(context,request))

def detail(request, student_first_name, student_last_name):
    return HttpResponse("Student details for %s %s:" %(student_first_name, student_last_name))

def update(request, student_first_name, student_last_name):
    return HttpResponse("Update student details for %s %s:" %(student_first_name, student_last_name))
