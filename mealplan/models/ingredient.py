from django.db import models
from .food import Food
from .recipe import Recipe
from .unit import Unit


class Ingredient(models.Model):
    """
    Ingredient model. A recipe can contain one or multiple ingredients
    and each ingredient can apply to at least one or multiple recipes.
    """
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True, default=1)

    def __str__(self):
        if self.unit:
            unit_name = self.unit.plural_name if self.amount > 1 else self.unit.name
            amount_str = str(int(self.amount)) if self.amount and self.amount.is_integer() and self.amount % 1 == 0 else str(self.amount)
            return f"{amount_str} {unit_name} de {self.food.name} dans {self.recipe.name}"
        else:
            amount_str = str(int(self.amount)) if self.amount and self.amount.is_integer() and self.amount % 1 == 0 else str(self.amount)
            return f"{amount_str} {self.food.name} dans {self.recipe.name}"
