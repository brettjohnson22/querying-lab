from django.shortcuts import render
from django.db.models import Count
from .models import Student, Instructor, Course, StudentCourse


def index(request):
    return render(request, 'school/index.html')

def problem_one(request):
    # Find all students who have a GPA greater than 3.0. 
    # Order the data by highest GPAs first.

    context = {
        'students': None
    }
    return render(request, 'school/one.html', context)

def problem_two(request):
    # Find all instructors hired prior to 2010
    # Order by hire date

    context = {
        'instructors': None
    }
    return render(request, 'school/two.html', context)

def problem_three(request):
    # Find all students who have a B+ in any class. 
    # Order the data by student's first name alphabetically.

    context = {
        'student_courses': None
    }
    return render(request, 'school/three.html', context)

def problem_four(request):
    # Find all students who are taking the Programming class. 
    # Order by their grade. 

    context = {
        'student_courses': None
    }
    return render(request, 'school/four.html', context)

def problem_five(request):
    # Find all students getting an A in the Programming class. 
    # Order by last name.

    context = {
        'student_courses': None
    }
    return render(request, 'school/five.html', context)

def problem_six(request):
    # Find all students with a GPA less than 3.0 who are getting an A in Programming class.
    # Order by GPA.

    context = {
        'student_courses': None
    }
    return render(request, 'school/six.html', context)

################## BONUS #################
# These problems will require using Aggregate functions along with annotate()
# https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
# https://docs.djangoproject.com/en/4.0/ref/models/querysets/#annotate

# BONUS ONE
# Find the instructor who is only teaching one single course

# BONUS TWO
# Display all students along with the number of credits they are taking

# BONUS THREE
# Find all students who are getting an A in any course and average their GPAs. Display the number of students and their Average GPA