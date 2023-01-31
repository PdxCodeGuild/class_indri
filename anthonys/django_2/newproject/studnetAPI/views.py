from rest_framework import generics
from . models import Student
from .serializers import StudentSerializer

class ListStudents(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class ChangeStudents(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# create a new student
# retrieve a single student
# update a single student
# delete a single student

# from rest_framework import generics
# from todos.models import Todo
# from .serializers import TodoSerializer


# class ListTodos(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class ListCompletedTodos(generics.ListCreateAPIView):
#     queryset = Todo.objects.filter(completed=True)
#     serializer_class = TodoSerializer


# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer