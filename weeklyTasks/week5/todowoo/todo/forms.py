from django.forms import ModelForm
from .models import *

class toDoForm(ModelForm):
    
    class Meta:
        model = toDo
        fields = ('title', 'memo', 'important',)
