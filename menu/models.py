from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="pizzas",
    )

    def __str__(self):
        return self.name


class PizzaSize(models.Model):
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        related_name="sizes",
    )

    size = models.CharField(max_length=20)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.pizza.name} - {self.size}"
