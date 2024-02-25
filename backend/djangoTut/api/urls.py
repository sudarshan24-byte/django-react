from django.urls import path
from .views import *

urlpatterns = [
    path('cars/', cars),
    path('cars/create', createCar),
]
