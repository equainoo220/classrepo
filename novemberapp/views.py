from django.shortcuts import render
from .models import Student
from .converter import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# Writing the GET REQUEST for all students

@api_view(['GET'])
def getstudents(request):
    students = Student.objects.all()
    serial = StudentSerializer(students, many=True)
    return Response(serial.data)

# writing a POST request for a student
# this will allow the api to create a record

@api_view(['POST'])
def createstudent(request):
    serial = StudentSerializer(data = request.data)
    if serial.is_valid():
        serial.save()
        return Response(serial.data, status=status.HTTP_201_CREATED)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getmodifydelete(request, cnumber):
    try:
        students = Student.objects.get(cnumber=cnumber)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = StudentSerializer(students)
        return Response(serial.data)
    elif request.method == 'DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serial = StudentSerializer(students, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        