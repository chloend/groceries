"""
Tests for Unit model
"""
from django.core.exceptions import ValidationError
from django.test import TestCase

from recipe.models import Unit


class UnitTests(TestCase):
    """Test Unit model"""

    def test_create_unit(self):
        """Test creating a unit"""
        unit = Unit.objects.create(name="Kilogram", short_name="kg", plural_name="Kilograms")
        self.assertEqual(unit.name, "Kilogram")
        self.assertEqual(unit.short_name, "kg")
        self.assertEqual(unit.plural_name, "Kilograms")

    def test_create_unit_with_empty_name(self):
        """Test creating a unit with empty name"""
        with self.assertRaises(ValidationError):
            Unit.objects.create(name="")

    def test_create_unit_with_invalid_characters(self):
        """Test creating a unit with invalid characters"""
        invalid_names = ["12345", "@#$%", "Kilogram1", "Kilogram!"]
        for name in invalid_names:
            with self.assertRaises(ValidationError):
                Unit.objects.create(name=name)

    def test_unit_name_max_length(self):
        """Test that unit name cannot exceed max_length"""
        max_length = Unit._meta.get_field('name').max_length
        unit = Unit(name='A' * (max_length + 1))

        # Note: For required fields, it's recommended to use full_clean()
        # instead of create(). The create() method does not automatically
        # enforce model field constraints such as max_length. Using full_clean()
        # ensures that all model validations, including max_length, are properly
        # checked before saving the object to the database. This is especially
        # important to prevent invalid data from being saved in cases where the
        # admin interface or other forms might bypass client-side validations.
        with self.assertRaises(ValidationError):
            unit.full_clean()
            unit.save()

    def test_unit_short_name_max_length(self):
        """Test that unit short name cannot exceed max_length"""
        max_length = Unit._meta.get_field('short_name').max_length

        with self.assertRaises(ValidationError):
            Unit.objects.create(short_name='A' * (max_length + 1))

    def test_unit_plural_name_max_length(self):
        """Test that unit plural name cannot exceed max_length"""
        max_length = Unit._meta.get_field('plural_name').max_length

        with self.assertRaises(ValidationError):
            Unit.objects.create(plural_name='A' * (max_length + 1))
