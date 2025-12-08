from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .model.todo_model import Todo
from .serializer.todo_serializer import TodoSerializer


class TodoView(APIView):

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Created successfully", "data": serializer.data})
        return Response(serializer.errors, status=400)

    def get(self, request, id=None):
        if id:
            try:
                todo = Todo.objects.get(id=id)
                serializer = TodoSerializer(todo)
                return Response(serializer.data)
            except Todo.DoesNotExist:
                return Response({"error": "Not found"}, status=404)

        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


    def put(self, request, id=None):
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        serializer = TodoSerializer(todo, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response({"message": "Deleted"})
        except Todo.DoesNotExist:
            return Response({"error": "Not found"}, status=404)