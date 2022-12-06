from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


def home(request):
    context = {
        'title': 'Home Page'
    }
    return render(request, 'halls/index.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


# def create_hall(request):
#     if request.method == 'POST':
#     pass

class CreateHall(generic.CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('home')