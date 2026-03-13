from django.db import models
from users.models import TelegramUser
from menu.models import Pizza


class CartItem(models.Model):

    user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE
    )

    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user} - {self.pizza}"