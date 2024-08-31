"""
Unit model
"""
from django.db import models
from django.core.exceptions import ValidationError

import re


class Unit(models.Model):
    """Unit object"""
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10, blank=True, null=True)
    plural_name = models.CharField(max_length=50, blank=True, null=True)

    def clean(self):
        """Clean Unit fields before validation"""
        valid_field_regex = re.compile(r'^[A-Za-z\s]+$')

        # Validate `name`
        if not valid_field_regex.match(self.name):
            raise ValidationError({'name': 'The name should only contain letters and spaces.'})

        # Validate `short_name`
        if self.short_name and not valid_field_regex.match(self.short_name):
            raise ValidationError({'short_name': 'The short name should only contain letters and spaces.'})

        # Validate `plural_name`
        if self.plural_name and not valid_field_regex.match(self.plural_name):
            raise ValidationError({'plural_name': 'The plural name should only contain letters and spaces.'})

    def svae(self, *args, **kwargs):
        """Save Unit in database"""
        self.clean()
        super.save(*args, **kwargs)

    def __str__(self):
        return self.name
