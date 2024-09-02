"""
Tests for Category model
"""
from django.core.exceptions import ValidationError
from django.test import TestCase

from recipe.models import Category


class CategoryTests(TestCase):
    """Test Category model"""

    def test_create_category(self):
        """Test creating a category"""
        category = Category.objects.create(name="Vegetarian")
        self.assertEqual(category.name, "Vegetarian")

    def test_create_category_with_empty_name(self):
        """Test creating a category with an empty name"""
        category = Category(name="")
        with self.assertRaises(ValidationError):
            category.full_clean()
            category.save()

    def test_create_category_with_invalid_characters(self):
        """Test creating a category with invalid characters"""
        invalid_names = ["12345", "@#$%", "Vegetarian1", "Vegetarian!"]
        for name in invalid_names:
            with self.assertRaises(ValidationError):
                category = Category(name=name)
                category.full_clean()
                category.save()

    def test_create_category_with_dupplicate_names(self):
        """Test creating two categories with the same names but different cases"""
        Category.objects.create(name="Dessert")
        with self.assertRaises(ValidationError):
            Category.objects.create(name="dessert")

    def test_category_name_max_length(self):
        """Test that category name cannot exceed max_length"""
        max_length = Category._meta.get_field('name').max_length
        category = Category(name='A' * (max_length + 1))

        # Note: For required fields, it's recommended to use full_clean()
        # instead of create(). The create() method does not automatically
        # enforce model field constraints such as max_length. Using full_clean()
        # ensures that all model validations, including max_length, are properly
        # checked before saving the object to the database. This is especially
        # important to prevent invalid data from being saved in cases where the
        # admin interface or other forms might bypass client-side validations.
        with self.assertRaises(ValidationError):
            category.full_clean()
            category.save()
