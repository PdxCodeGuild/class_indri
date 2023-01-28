from django.shortcuts import render
from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer

def index(request):
    return render(request, 'studentapp/index.html')

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class StudentActions(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
        
class StudentSearch(generics.ListAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        first_name = self.kwargs['first_name']
        return Student.objects.filter(first_name=first_name)

        


