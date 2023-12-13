from django.db import models
from .ingredient import Ingredient

class ShoppingList(models.Model):
    ingredients = models.ManyToManyField(Ingredient)

    def get_ingredient_names(self):
        return [ingredient.food.name for ingredient in self.ingredients.all()]