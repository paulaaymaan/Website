from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    desired_weight = models.DecimalField(max_digits=5, decimal_places=2)


class DietPlan(models.Model):
    MEAL_CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Snack', 'Snack'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
   # meal = models.CharField(max_length=50, choices=MEAL_CHOICES)
    Breakfast = models.CharField(max_length=500)
    Snack = models.CharField(max_length=500)
    Lunch = models.CharField(max_length=500)
    Dinner = models.CharField(max_length=500)
