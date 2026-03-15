from django.test import TestCase
from users.models import TelegramUser
from orders.models import Order


class OrderTest(TestCase):

    def setUp(self):

        self.user = TelegramUser.objects.create(
            telegram_id=1,
            first_name="Test"
        )

    def test_create_order(self):

        order = Order.objects.create(
            user=self.user
        )

        self.assertEqual(order.user, self.user)