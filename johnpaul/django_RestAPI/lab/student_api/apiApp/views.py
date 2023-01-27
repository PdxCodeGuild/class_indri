from rest_framework import generics
from students.models import Student
from .serializers import StudentSerializer




class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentFilter(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        capstone = self.request.query_params.get('capstone', None)
        if capstone is not None:
            queryset = queryset.filter(name=capstone)
        return queryset
