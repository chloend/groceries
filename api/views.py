# api/views.py
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from mealplan.models import Recipe
from .serializers import RecipeDetailSerializer, RecipeListSerializer


class RecipeDetailsAPIView(APIView):
    def get(self, _, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        serializer = RecipeDetailSerializer(recipe)
        return Response(serializer.data)


class RecipeListAPIView(APIView):
    def get(self, request):
        search_value = request.query_params.get('search', '')
        category_values = request.query_params.getlist('categories')

        recipes = Recipe.objects.all()

        if search_value:
            recipes = recipes.filter(name__icontains=search_value)

        if category_values:
            category_filter = Q()
            for category_value in category_values:
                category_filter |= Q(categories__name=category_value)
            recipes = recipes.filter(category_filter)
        
        serializer = RecipeListSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)