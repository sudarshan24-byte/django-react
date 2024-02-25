from django.urls import path
from .views import *

urlpatterns = [
    path('', cars),
    path('cars/create', createCar),
]
