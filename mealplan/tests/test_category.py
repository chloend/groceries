"""
Tests for Category model
"""
from django.core.exceptions import ValidationError
from django.test import TestCase

from mealplan.models import Category


class CategoryTests(TestCase):
    """Test Category model"""

    def test_create_category(self):
        """Test creating a category"""
        category = Category.objects.create(name="Vegetarian")
        self.assertEqual(category.name, "Vegetarian")

    def test_create_category_with_empty_name(self):
        """Test creating a category with an empty name"""
        with self.assertRaises(ValidationError):
            Category.objects.create(name="")

    def test_create_category_with_invalid_characters(self):
        """Test creating a category with invalid characters"""
        invalid_names = ["12345", "@#$%", "Vegetarian1", "Vegetarian!"]
        for name in invalid_names:
            with self.assertRaises(ValidationError):
                Category.objects.create(name=name)

    def test_create_category_with_dupplicate_names(self):
        """Test creating two categories with the same names but different cases"""
        Category.objects.create(name="Dessert")
        with self.assertRaises(ValidationError):
            Category.objects.create(name="dessert")
