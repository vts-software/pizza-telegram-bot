from django.urls import path
from .views import pizza_list

urlpatterns = [
    path("pizzas/", pizza_list)
]