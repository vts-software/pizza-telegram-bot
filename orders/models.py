from django.db import models
from users.models import User


class Order(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("processing", "Processing"),
        ("delivered", "Delivered"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
    )

    address = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"