from datetime import datetime
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *

def home(reqeust):
    context = {
        'title': 'Home'
    }
    return render(request=reqeust, template_name='todo/index.html', context=context)

def signup(request):
    context = {
        'title': 'Sign Up'
    }
    form = UserCreationForm()
    context['form'] = form
    if request.method == 'GET':
        pass    
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
            except IntegrityError:
                context['error'] = 'That user already exists'
        else:
            context['error'] = 'Passoword doesnt match!'
    return render(request=request, template_name='todo/signup.html', context=context)

def signin(request):
    context = {
        'title': 'Sign In'
    }
    form = AuthenticationForm()
    context['form'] = form
    if request.method == 'GET':
        pass
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('todolist')
        else:
            context['error'] = 'Username or password ar wrong!'
    return render(request=request, template_name='todo/signin.html', context=context)


@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('todolist')


@login_required(login_url='signin')
def todolist(request):
    context = {
        'title': 'To Do List'
    }
    todolist = toDo.objects.filter(user=request.user, dateCompleted__isnull=True)
    context['todos'] = todolist
    return render(request, 'todo/todolist.html', context=context)


@login_required(login_url='signin')
def createToDo(request):
    context = {
        'title': 'Create To Do'
    }
    form = toDoForm()
    context['form'] = form
    if request.method == 'POST':
        try:
            form = toDoForm(request.POST)        
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todolist')
        except:
            context['error'] = 'Bad Data!!! Try again'
    return render(request, 'todo/createToDo.html', context=context)


@login_required(login_url='signin')
def toDoDetail(request, pk):
    todo = toDo.objects.get(pk=pk, user=request.user)
    context = {
        'title': todo.title,
        'todo': todo
    }
    form = toDoForm(instance=todo) 
    context['form'] = form 
    if request.method == 'POST':
        try:
            form = toDoForm(request.POST, instance=todo)
            form.save()
            return redirect('todolist')
        except:
            context['error'] = 'Something wrong'
            pass
    return render(request, 'todo/tododetail.html', context)


@login_required(login_url='signin')
def toDoComlete(request, pk):
    todo = toDo.objects.get(pk=pk, user=request.user)
    context = {
        'title': todo.title,
        'todo': todo
    } 
    if request.method == 'POST':
        todo.dateCompleted = datetime.now()
        todo.save()
        return redirect('todolist')
    return render(request, 'todo/tododetail.html', context)


@login_required(login_url='signin')
def toDoDelete(request, pk):
    todo = toDo.objects.get(pk=pk, user=request.user)
    context = {
        'title': todo.title,
        'todo': todo
    } 
    if request.method == 'POST':
        todo.delete()
        return redirect('todolist')
    return render(request, 'todo/tododetail.html', context)


@login_required(login_url='signin')
def completed(request):
    context = {
        'title': 'Completed To Do`s'
    }
    todolist = toDo.objects.filter(user=request.user, dateCompleted__isnull=False)
    context['todos'] = todolist
    return render(request, 'todo/completed.html', context=context)