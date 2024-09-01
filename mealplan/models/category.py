"""
Category model
"""
from django.db import models
from django.core.exceptions import ValidationError

import re


class Category(models.Model):
    """Category object"""
    name = models.CharField(max_length=100, unique=True)

    def clean(self):
        """Clean category name field before validation"""
        if not self.name:
            raise ValidationError({'name': 'The name field cannot be empty.'})
        if not re.match(r'^[a-zA-Z\s]+$', self.name):
            raise ValidationError({'name': 'The name field must contain only letters and spaces.'})
        if Category.objects.filter(name__iexact=self.name).exists():
            raise ValidationError({'name': 'A category with this name already exists.'})

    def save(self, *args, **kwargs):
        """Save Category in database"""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
