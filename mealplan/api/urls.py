# api/urls.py

from django.urls import path
from .views import RecipeDetailsAPIView, RecipeListAPIView

urlpatterns = [
    path('recipes/<slug:slug>/', RecipeDetailsAPIView.as_view(), name='recipe-detail-api'),
    path('recipes/', RecipeListAPIView.as_view(), name='recipe-list-api'),
]