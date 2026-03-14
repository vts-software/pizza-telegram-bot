from django.test import TestCase
from users.models import TelegramUser


class BotLogicTest(TestCase):

    def test_create_telegram_user(self):

        user = TelegramUser.objects.create(
            telegram_id=999,
            first_name="BotUser"
        )

        self.assertEqual(user.telegram_id, 999)