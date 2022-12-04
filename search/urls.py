from django.urls import path, include
from .views import ValueSearching,GoogelSearchAPI
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('search', GoogelSearchAPI, basename='searching')





urlpatterns = [
    path('search/show/', ValueSearching),
    path("", include(router.urls)),

]
