from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import loader
from django.http import HttpResponse

from todo.models import Todo
from todo.serializers import TodoSerializer


@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def web_list(request):
    if request.method == 'GET':
        todo_list = Todo.objects.all()
        template = loader.get_template('todo/index.html')
        context = {
            'todo_list': todo_list,
        }
        return HttpResponse(template.render(context, request))

@api_view(['GET'])
def web_new(request):
    if request.method == 'GET':
        template = loader.get_template('todo/new.html')
        context = {
        }
        return HttpResponse(template.render(context, request))

@api_view(['GET'])
def web_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        template = loader.get_template('todo/detail.html')
        context = {
            'todo': todo,
        }
        return HttpResponse(template.render(context, request))
