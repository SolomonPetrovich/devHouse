from django.shortcuts import render
from .models import *

def home(requests):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(requests, template_name='portfolio/index.html', context=context)