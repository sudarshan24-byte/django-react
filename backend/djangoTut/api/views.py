from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CarSerializer

# Create your views here.

@api_view(['GET'])
def cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def createCar(request):
    data = request.data
    serializer = CarSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  # 201 Created status for successful creation
    return Response(serializer.errors, status=400)