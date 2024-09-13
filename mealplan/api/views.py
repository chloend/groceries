# api/views.py
from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView

from recipe.models import Recipe
from .serializers import RecipeDetailSerializer, RecipeListSerializer


class RecipeDetailsAPIView(RetrieveAPIView):
    queryset = Recipe.objects.prefetch_related('categories', 'ingredients').all()
    serializer_class = RecipeDetailSerializer
    lookup_field = 'slug'


class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.prefetch_related('categories').all()
    serializer_class = RecipeListSerializer

    def get_queryset(self):
        search_value = self.request.query_params.get('search', '')
        category_values = self.request.query_params.getlist('categories')

        queryset = self.queryset

        # Use of Q() query to combine search and category values
        query_filter = Q()

        if search_value: # Name search
            query_filter &= Q(name__icontains=search_value)

        if category_values: # Cateogry filter
            category_filter = Q()
            for category_value in category_values:
                category_filter |= Q(categories__name=category_value)
            query_filter &= category_filter

        # Apply filters combined to queryset
        queryset = queryset.filter(query_filter)

        return queryset