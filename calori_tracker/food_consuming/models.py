from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()


class FoodConsuming(models.Model):
    user = models.ForeignKey(User)
    food = models.ForeignKey(Food)
