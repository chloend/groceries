from django.contrib import admin
from .models import *


@admin.display(description="Ingrédients de la recette")
def get_ingredient(recipe):
    return ", ".join(list(recipe.ingredients.values_list("name", flat=True)))


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]


admin.site.register(Category)
admin.site.register(Day)
admin.site.register(Food)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Unit)
admin.site.register(ShoppingList)
