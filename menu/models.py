from django.db import models


class Pizza(models.Model):

    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.size}"