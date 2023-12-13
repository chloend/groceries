# mealplan/views.py

from django.shortcuts import render, get_object_or_404
from .models import Category, Ingredient, Recipe


def home(request):
    return render(request, 'mealplan/home.html')


def recipe_list(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()

    selected_categories = request.GET.getlist('categories')

    if selected_categories:
        recipes = recipes.filter(categories__id__in=selected_categories)

    return render(request, 'mealplan/recipe_list.html', {'recipes': recipes, 'categories': categories})


def recipe_detail(request, recipe_name):
    recipe = get_object_or_404(Recipe, slug=recipe_name)
    ingredients_list = Ingredient.objects.filter(recipe__id=recipe.id)

    context = {
        "recipe": recipe,
        "ingredients_list": ingredients_list,
    }
    return render(request, 'mealplan/recipe_detail.html', context)
