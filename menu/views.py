from rest_framework import generics
from .models import Category, Pizza
from .serializers import CategorySerializer, PizzaSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PizzaListView(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer