from django.db import models


class Food(models.Model):
    """
    Food model has a many-to-many relationship with recipe model.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"
