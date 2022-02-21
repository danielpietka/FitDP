from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    def __str__(self):
        return self.name
    FOOD_TYPE = (
        ("Meat", "Meat"),
        ("Egg", "Egg"),
        ("Dairy products", "Dairy products"),
        ("Nuts", "Nuts"),
        ("Breads", "Breads"),
        ("Spices", "Spices"),
        ("Seafood", "Seafood"),
        ("Candies", "Candies"),
        ("Desserts", "Desserts"),
        ("Fruits", "Fruits"),
        ("Vegetables", "Vegetables"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    kcal = models.IntegerField()
    type = models.CharField(
        max_length=30,
        choices=FOOD_TYPE)
