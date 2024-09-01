"""
Tests for Ingredient model
"""
from django.core.exceptions import ValidationError
from django.test import TestCase

from mealplan.models import Food, Ingredient, Recipe, Unit


class IngredientTests(TestCase):
    """Test Ingredient model"""

    def test_create_ingredient(self):
        """Test creating an ingredient with valid data"""
        food = Food.objects.create(name="Flour")
        recipe = Recipe.objects.create(name="Cookie", servings=12, slug="cookie")
        unit = Unit.objects.create(name="gram", short_name="gr", plural_name="grams")
        ingredient = Ingredient.objects.create(food=food, recipe=recipe, amount=220, unit=unit)

        self.assertEqual(ingredient.food.name, "Flour")
        self.assertEqual(ingredient.recipe.name, "Cookie")
        self.assertEqual(ingredient.amount, 220)
        self.assertEqual(ingredient.unit.name, "gram")

    def test_create_ingredient_without_unit(self):
        """Test creating an ingredient without a unit"""
        food = Food.objects.create(name="Egg")
        recipe = Recipe.objects.create(name="Cookie", servings=12, slug="cookie")
        ingredient = Ingredient.objects.create(food=food, recipe=recipe, amount=1)

        self.assertEqual(ingredient.unit, None)
        self.assertEqual(str(ingredient), "1 Egg in Cookie")

    def test_create_ingredient_without_amount(self):
        """Test creating an ingredient without specifying an amount."""
        food = Food.objects.create(name="Salt")
        recipe = Recipe.objects.create(name="Cookie", servings=12, slug="cookie")
        ingredient = Ingredient(food=food, recipe=recipe)

        self.assertIsNone(ingredient.amount)
        self.assertEqual(str(ingredient), "Salt in Cookie")

    def test_create_ingredient_with_non_numeric_amount(self):
        """Test creating an ingredient with a non-numeric amount."""
        food = Food.objects.create(name="Salt")
        recipe = Recipe.objects.create(name="Cookie", servings=12, slug="cookie")

        with self.assertRaises(ValidationError):
            Ingredient.objects.create(food=food, recipe=recipe, amount="invalid")
