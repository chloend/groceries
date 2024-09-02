from django.db import models
from django.urls import reverse
from .category import Category
from .food import Food


class Recipe(models.Model):
    """
    The information of a recipe. The Recipe model has a many-to-many relationship
    with the Ingredient model. See Ingredient model for more information.
    """
    name = models.CharField(max_length=200)
    servings = models.IntegerField()
    ingredients = models.ManyToManyField(Food, through="Ingredient")
    categories = models.ManyToManyField(Category)
    description = models.TextField(default="Pas encore de description :o")
    slug = models.SlugField(null=False, unique=True, max_length=200)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})
