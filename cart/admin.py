from django.db import models
from users.models import TelegramUser


class Order(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("paid", "Paid"),
        ("done", "Done"),
    ]

    user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE
    )

    total_price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"