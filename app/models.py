from django.contrib.auth.models import User
from django.db import models


class Food(models.Model):
    # Item name in admin
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    carbohydrates = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)