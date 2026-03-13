from rest_framework import serializers
from .models import Category, Pizza, PizzaSize

class PizzaSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaSize
        fields = ["id","size","price"]

class PizzaSerializer(serializers.ModelSerializer):
    sizes = PizzaSizeSerializer(many=True,read_only=True)

    class Meta:
        model = Pizza
        fields = ["id","name","description","sizes"]

class CategorySerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True,read_only=True)

    class Meta:
        model = Category
        fields = ["id","name","pizzas"]