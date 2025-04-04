from django.shortcuts import render
from rest_framework import viewsets
from. models import *
from .serializers import *
# Create your views here.

class bookviewset(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=Bookserializers
