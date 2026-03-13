from django.db import models

from users.models import User
from menu.models import PizzaSize


class CartItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cart_items",
    )

    pizza_size = models.ForeignKey(
        PizzaSize,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user} - {self.pizza_size}"# Create your models here.
