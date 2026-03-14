from django.test import TestCase
from .models import TelegramUser


class TelegramUserTest(TestCase):

    def test_create_user(self):

        user = TelegramUser.objects.create(
            telegram_id=123456,
            username="test_user",
            first_name="John"
        )

        self.assertEqual(user.telegram_id, 123456)
        self.assertEqual(user.first_name, "John")