"""
Views for recipe web app
"""
from django.shortcuts import render, get_object_or_404
from .models import Category, Ingredient, Recipe


def home(request):
    return render(request, 'recipe/home.html')


def recipe_list(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.prefetch_related('categories').all()

    selected_categories = request.GET.getlist('categories')

    if selected_categories:
        recipes = recipes.filter(categories__id__in=selected_categories)

    return render(request, 'recipe/recipe_list.html', {'recipes': recipes, 'categories': categories})


def recipe_detail(request, recipe_name):
    recipe = get_object_or_404(Recipe.objects.prefetch_related('categories'), slug=recipe_name)
    ingredients_list = Ingredient.objects.filter(recipe=recipe).select_related('food', 'unit')

    context = {
        "recipe": recipe,
        "ingredients_list": ingredients_list,
    }
    return render(request, 'recipe/recipe_detail.html', context)
