"""
Test for Food model
"""
from django.core.exceptions import ValidationError
from django.test import TestCase

from mealplan.models import Food


class FoodTests(TestCase):
    """Test Food model"""

    def test_create_food(self):
        """Test creating food"""
        food = Food.objects.create(name="Apple")
        self.assertEqual(food.name, "Apple")

    def test_create_food_with_empty_name(self):
        """Test creating food with empty name"""
        with self.assertRaises(ValidationError):
            Food.objects.create(name="")

    def test_create_food_with_invalid_characters(self):
        """Test creating a category with invalid characters"""
        invalid_names = ["12345", "@#$%", "Vegetarian1", "Vegetarian!"]
        for name in invalid_names:
            with self.assertRaises(ValidationError):
                Food.objects.create(name=name)

    def test_create_food_with_dupplicate_names(self):
        """Test creating food with the same names but different cases"""
        Food.objects.create(name="Apple")

        with self.assertRaises(ValidationError):
            Food.objects.create(name="apple")

    def test_food_name_max_length(self):
        """Test checking food name cannot exceed max_length"""
        max_length = Food._meta.get_field('name').max_length
        food = Food(name='A' * (max_length + 1))

        # Note: For required fields, it's recommended to use full_clean()
        # instead of create(). The create() method does not automatically
        # enforce model field constraints such as max_length. Using full_clean()
        # ensures that all model validations, including max_length, are properly
        # checked before saving the object to the database. This is especially
        # important to prevent invalid data from being saved in cases where
        # the admin interface or other forms might bypass client-side validations.
        with self.assertRaises(ValidationError):
            food.full_clean()
            food.save()
