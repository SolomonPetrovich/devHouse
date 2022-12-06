from django.db import IntegrityError
from django.shortcuts import render
from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser
from .serializers import *
from todo.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'Couldn`t login. Please check username or password'})
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            
            return JsonResponse({'token': str(token)}, status=200)


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(username=data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'That user already exists'}, status=400)



class ToDoCompletedList(generics.ListAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return toDo.objects.filter(user=user, dateCompleted__isnull=False).order_by('-dateCompleted')



class ToDoListCreate(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return toDo.objects.filter(user=user, dateCompleted__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ToDoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return toDo.objects.filter(user=user)


class ToDoComplete(generics.UpdateAPIView):
    serializer_class = ToDoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return toDo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.dateCompleted = timezone.now()
        serializer.save()

