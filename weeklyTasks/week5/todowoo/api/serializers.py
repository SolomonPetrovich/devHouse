from rest_framework import serializers
from todo.models import *

class ToDoSerializer(serializers.ModelSerializer):
    dateCreated = serializers.ReadOnlyField()
    dateCompleted = serializers.ReadOnlyField()

    class Meta:
        model = toDo
        fields = ['id', 'title', 'memo', 'dateCreated', 'dateCompleted', 'important']


class ToDoCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = toDo
        fields = ['id']
        read_only_fields = ['title', 'memo', 'dateCreated', 'dateCompleted', 'important']