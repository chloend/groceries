# mealplan/urls.py

from django.urls import path
from .views import home, recipe_list, recipe_detail

app_name = "mealplan"

urlpatterns = [
    path('', home, name="home"),
    path('recipes/', recipe_list, name="recipe-list"),
    path('recipes/<slug:recipe_name>/', recipe_detail, name="recipe-detail"),
]