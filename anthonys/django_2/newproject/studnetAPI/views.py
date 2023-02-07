from rest_framework import generics
from . models import Student
from .serializers import StudentSerializer

class ListStudents(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class ChangeStudents(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
