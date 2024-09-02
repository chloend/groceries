"""
Tests for Recipe model
"""
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.test import TestCase

from recipe.models import Category, Food, Ingredient, Recipe, Unit


class RecipeTests(TestCase):
    """Test Recipe model"""

    def test_create_recipe(self):
        """Test creating a recipe"""

        # Create categories
        category1 = Category.objects.create(name="Dessert")
        category2 = Category.objects.create(name="Snack")

        # Create foods
        food1 = Food.objects.create(name="Chocolate chips")
        food2 = Food.objects.create(name="Butter")

        # Create units
        unit = Unit.objects.create(name="gram")

        # Create recipe
        recipe = Recipe.objects.create(
            name="Chocolate chip cookies",
            servings=12,
            description="Easy homemade cookies",
            slug="chocolate-chip-cookies"
        )

        # Create ingredients
        ingredient1 = Ingredient.objects.create(
            food=food1,
            recipe=recipe,
            amount=100,
            unit=unit
        )

        ingredient2 = Ingredient.objects.create(
            food=food2,
            recipe=recipe,
            amount=120,
            unit=unit
        )

        # Add categories and foods to recipe
        recipe.categories.add(category1, category2)
        recipe.ingredients.add(food1, food2)

        # Assertions
        self.assertEqual(recipe.name, "Chocolate chip cookies")
        self.assertEqual(recipe.servings, 12)
        self.assertEqual(recipe.description, "Easy homemade cookies")
        self.assertEqual(recipe.slug, "chocolate-chip-cookies")

        # Check categories
        self.assertEqual(recipe.categories.count(), 2)
        self.assertTrue(recipe.categories.filter(name="Dessert").exists())
        self.assertTrue(recipe.categories.filter(name="Snack").exists())

        # Check ingredients total
        ingredients = recipe.ingredients.all()
        self.assertEqual(ingredients.count(), 2)

        # Expected data
        expected_data = {
            ingredient1: {'food_name': 'Chocolate chips', 'amount': 100, 'unit': unit},
            ingredient2: {'food_name': 'Butter', 'amount': 120, 'unit': unit},
        }

        # Chech food name, amounts and units for each ingredient
        for ingredient, data in expected_data.items():
            self.assertEqual(ingredient.food.name, data['food_name'])
            self.assertEqual(ingredient.amount, data['amount'])
            self.assertEqual(ingredient.unit, data['unit'])
