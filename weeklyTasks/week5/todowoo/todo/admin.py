from django.contrib import admin
from .models import *

class toDoAdmin(admin.ModelAdmin):
    readonly_fields = ('dateCreated', )

admin.site.register(toDo, toDoAdmin)