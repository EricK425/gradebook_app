from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Student

# Create your views here.
def index(request):
    all_students = Student.objects.order_by('last_name')
    context = {
        'all_students': all_students,
    }
    return render(request, 'students/index.html', context)

def detail(request, student_first_name, student_last_name):
    return HttpResponse("Student details for %s %s:" %(student_first_name.title(), student_last_name.title()))

def update(request, student_first_name, student_last_name):
    return HttpResponse("Update student details for %s %s:" %(student_first_name, student_last_name))
