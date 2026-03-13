from django.urls import path
from .views import CategoryListView, PizzaListView

urlpatterns = [
    path("categories/", CategoryListView.as_view()),
    path("pizzas/", PizzaListView.as_view()),
]