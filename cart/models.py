from django.db import models
from menu.models import Pizza
from users.models import TelegramUser


class Cart(models.Model):

    user = models.OneToOneField(
        TelegramUser,
        on_delete=models.CASCADE,
        related_name="cart"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user}"


class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )

    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("cart", "pizza")

    def __str__(self):
        return f"{self.pizza} x {self.quantity}"