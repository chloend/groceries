from rest_framework import serializers
from mealplan.models import Category, Recipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class RecipeDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    ingredients = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['name', 'categories', 'servings', 'ingredients', 'description', 'slug']

    def get_ingredients(self, obj):
        # obj.ingredient_set.all() returns Ingredient objects list related to Recipe
        return [
            {'food': ingredient.food.name, 
             'amount': ingredient.amount, 
             'unit': {
                 'name': ingredient.unit.name,
                 'short_name': ingredient.unit.short_name,
                 'plural_name': ingredient.unit.plural_name,
                 } if ingredient.unit else None,
            }
            for ingredient in obj.ingredient_set.all()
        ]


class RecipeListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['name', 'slug', 'categories']
