from django.db import models


class Unit(models.Model):
    """
    The measurement of an ingredient.
    """
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10, blank=True, null=True)
    plural_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
