from django.shortcuts import render
from rest_framework import generics
from .models import Students
from .serializers import StudentSerializer


# Create your views here.
class AllStudents(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

# class SelectStudent(generics.ListCreateAPIView):
#     queryset = Students.objects.filter(capstone = "")
#     serializer_class = StudentSerializer

class DetailStudents(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer