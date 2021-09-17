from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import *

# Create your views here.
class TodoView(APIView):
    # parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
      todos=Todo.objects.all()
      serlializer=TodoSerializer(todos, many=True)
      return Response(serlializer.data)

    def post(self, request, *args, **kwargs):
      serlializer= TodoSerializer(data=request.data)
      if serlializer.is_valid():
        serlializer.save()
      return Response(serlializer.data)

@api_view(['POST'])
def UpdateTodo(request, pk):
	todo = Todo.objects.get(id=pk)
	serializer = TodoSerializer(instance=todo, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteTodo(request, pk):
  todo = Todo.objects.get(id=pk)
  todo.delete()
  return Response('Todo was deleted')

@api_view(['POST'])
def CheckTodo(request, pk):
  todo = Todo.objects.filter(id=pk)
  reverse=todo[0].checked
  todo.update(checked=not reverse)
  print("filter hihi ", reverse)
  return Response("lol")


