from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from pages.models import Task
import requests

from pages.serializers import Taskserializer

# Create your views here.
# @api_view(['GET'])
def home(request):
    info = requests.get('https://jsonplaceholder.typicode.com/users')
    data = info.json()
    return render(request, 'home.html', {'data':data})
    # context = {
    #     'All Task': 'https://localhost:8000/alltask',
    #     'Create Task': 'https://localhost:8000/createtask',
    #     'Edit Task': 'https://localhost:8000/edittask/id',
    #     'View Task': 'https://localhost:8000/viewtask/id',
    #     'Delete Task': 'https://localhost:8000/deletetask/id',
    # }
    # return Response(context)

@api_view(['POST'])
def createtask(request):
   record = Taskserializer(data=request.data)
   if record.is_valid():
       record.save()
   return Response(record.data)

@api_view(['GET'])
def alltask(request):
   record = Task.objects.all()
   record = Taskserializer(record, many=True)
   return Response(record.data)

@api_view(['DELETE'])
def deletetask(request, id):
    record = Task.objects.get(id=id)
    record.delete()
    return Response(Response.deleted())

@api_view(['PUT'])
def edittask(request, id):
    record =Task.objects.get(id=id)
    serilizer = Taskserializer(data= request.data, instance=record, many=False)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data)