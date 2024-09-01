"""
Ingredient model
"""
from django.db import models
from django.core.exceptions import ValidationError

from .food import Food
from .recipe import Recipe
from .unit import Unit


class Ingredient(models.Model):
    """Ingredient object"""
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)

    def clean(self):
        """Check ingredient amount field before validation"""
        if self.amount is not None and not isinstance(self.amount, (int, float)):
            raise ValidationError({'amount': 'The amount must be a number.'})

        if isinstance(self.amount, float) and self.amount < 0:
            raise ValidationError({'amount': 'The amount cannot be negative.'})

    def save(self, *args, **kwargs):
        """Save Ingredient in database"""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of an ingredient.

         The string includes the amount (if present), the unit (if present), the food name,
        and the recipe name. If the amount is not provided, the format will be:
        - "{food_name} dans {recipe_name}"

        If the amount is provided but no unit is specified, the format will be:
        - "{amount} {food_name} dans {recipe_name}"

        If both amount and unit are provided, the format will be:
        - "{amount} {unit_name} de {food_name} dans {recipe_name}"

        The method ensures no extra spaces are included if the unit is not provided.
        """
        if self.amount is None:
            return f"{self.food.name} in {self.recipe.name}"

        if isinstance(self.amount, float) and self.amount.is_integer():
            amount_str = str(int(self.amount))
        else:
            amount_str = str(self.amount)

        if self.unit:
            unit_name = self.unit.plural_name if self.amount > 1 else self.unit.name
            return f"{amount_str} {unit_name} of {self.food.name} in {self.recipe.name}"
        else:
            return f"{amount_str} {self.food.name} in {self.recipe.name}"
