from django.shortcuts import render

# Create your views here.
def django(request):
    return render(request,
                  'ex01/django.html',
                  {'title': "Ex01: Django, framework web."})

def display(request):
    return render(request,
                  'ex01/display.html',
                  {'title': "Ex01: Display process of a static page."})

def templates(request):
    return render(request,
                  'ex01/templates.html',
                  {'title': "Ex01: Template engine."})