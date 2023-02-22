from rest_framework import generics
from students.models import Student
from .serializers import StudentSerializer





class StudentCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        first_name = self.kwargs['first_name']
        return Student.objects.filter(first_name=first_name)
