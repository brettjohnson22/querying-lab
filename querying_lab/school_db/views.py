from django.shortcuts import render
from django.db.models import Count
from .models import Student, Instructor, Course, StudentCourse

# Create your views here.

def problem_one(request):
    # Find all students who have a GPA greater than 3.0. 
    # Order the data by highest GPAs first.

    context = {
        'students': None
    }
    return render(request, 'students/index.html', context)

def problem_two(request):
    # Find all students who have a B+ in any class. 
    # Order the data by first name alphabetically.

    context = {
        'students': None
    }
    return render(request, 'students/index.html', context)

def problem_three(request):
    # Find all students who are taking the Programming class. 
    # Order by their grade. 

    context = {
        'students': None
    }
    return render(request, 'students/index.html', context)

def problem_four(request):
    # Find all students getting an A in the Programming class. 
    # Order by last name.

    context = {
        'students': None
    }
    return render(request, 'students/index.html', context)

def problem_five(request):
    # Find all students with a GPA less than 3.0 who are getting an A in Programming class.
    # Order by GPA.

    context = {
        'students': None
    }
    return render(request, 'students/index.html', context)
