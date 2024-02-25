from django.db import models

# Create your models here.
class Car(models.Model):
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    top_speed = models.DecimalField(max_digits=10, decimal_places=5)
    hp = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    