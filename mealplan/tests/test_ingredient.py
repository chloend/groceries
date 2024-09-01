"""
Tests for Ingredient model
"""
from django.db.utils import IntegrityError
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

    def test_create_ingredient_with_different_recipe_or_food(self):
        """Test that creating an ingredient with a different recipe or food is allowed"""
        food1 = Food.objects.create(name="Flour")
        food2 = Food.objects.create(name="Salt")
        recipe1 = Recipe.objects.create(name="Cookie", servings=4, slug="cookie")
        recipe2 = Recipe.objects.create(name="Bread", servings=1, slug="bread")

        Ingredient.objects.create(food=food1, recipe=recipe1, amount=220)
        Ingredient.objects.create(food=food1, recipe=recipe2, amount=500)
        Ingredient.objects.create(food=food2, recipe=recipe1)
        Ingredient.objects.create(food=food2, recipe=recipe2)

        self.assertEqual(Ingredient.objects.count(), 4)

    def test_create_ingredient_with_non_numeric_amount(self):
        """Test creating an ingredient with a non-numeric amount."""
        food = Food.objects.create(name="Salt")
        recipe = Recipe.objects.create(name="Cookie", servings=12, slug="cookie")

        with self.assertRaises(ValidationError):
            Ingredient.objects.create(food=food, recipe=recipe, amount="invalid")

    def test_create_dupplicate_ingredient(self):
        """Test creating an ingredient that already exists"""
        food = Food.objects.create(name="Salt")
        recipe = Recipe.objects.create(name="Cookie", servings=12, slug="cookie")
        Ingredient.objects.create(recipe=recipe, food=food)

        with self.assertRaises(ValidationError):
            ingredient_dupplicate = Ingredient(recipe=recipe, food=food)
            ingredient_dupplicate.full_clean()
            ingredient_dupplicate.save()

    def test_create_ingredient_withoud_food(self):
        """Test creating an ingredient without food"""
        recipe = Recipe.objects.create(name="Cookie", servings=12, slug="cookie")
        unit = Unit.objects.create(name="gram", short_name="gr", plural_name="grams")

        with self.assertRaises(IntegrityError):
            Ingredient.objects.create(recipe=recipe, amount=120, unit=unit)

    def test_create_ingredient_without_recipe(self):
        """Test creating an ingredient without a recipe"""
        food = Food.objects.create(name="Butter")
        unit = Unit.objects.create(name="gram", short_name="gr", plural_name="grams")

        with self.assertRaises(IntegrityError):
            Ingredient.objects.create(food=food, amount=120, unit=unit)
