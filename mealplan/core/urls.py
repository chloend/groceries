# urls.py
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('recipe/', include('recipe.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
] + debug_toolbar_urls()