from django.shortcuts import render

# Create your views here.
def one(request):

    context = {}
    return render(request, 'students/student-list.html', context)