from rest_framework import generics
from todos.models import Todo
from .serializers import TodoSerializer


class ListTodos(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ListCompletedTodos(generics.ListCreateAPIView):
    queryset = Todo.objects.filter(completed=True)
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
