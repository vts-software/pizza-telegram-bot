from django.db import models


class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.telegram_id})"
