import random
from django.shortcuts import render
from string import digits, punctuation, ascii_lowercase, ascii_uppercase

from generator.models import Password


def index(request):
    context = {}
    return render(request, 'generator/index.html', context)


def generated_password(request):
    new_password = ''
    
    length = int(request.GET.get('length'))
    upper = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    symbols = request.GET.get('symbols')
    

    chars = list(ascii_lowercase)

    if upper:
        print('we are here')
        chars.extend(list(ascii_uppercase))
    if numbers:
        chars.extend(list(digits))
    if symbols:
        chars.extend(list(punctuation))    

    for i in range(length):
        new_password += random.choice(chars)
    
    p = Password(passwords=new_password)
    p.save()
    pass_list = Password.objects.all()
    print(pass_list)

    context = {
        'passwords' : pass_list
    }
    
    return render(request, 'generator/password.html', context)