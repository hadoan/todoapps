from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets 
from .serializers import TodoSerializer 
from .models import Todo                     # add this
class TodoView(viewsets.ModelViewSet):       # add this
    serializer_class = TodoSerializer          # add this
    queryset = Todo.objects.all() 