from django.test import TestCase

from users.models import TelegramUser
from menu.models import Pizza
from cart.models import Cart, CartItem


class CartTest(TestCase):

    def setUp(self):

        self.user = TelegramUser.objects.create(
            telegram_id=1,
            first_name="Test"
        )

        self.cart = Cart.objects.create(user=self.user)

        self.pizza = Pizza.objects.create(
            name="Pepperoni",
            description="Classic",
            size="M",
            price=15,
            available=True
        )

    def test_add_to_cart(self):

        item = CartItem.objects.create(
            cart=self.cart,
            pizza=self.pizza,
            quantity=2
        )

        self.assertEqual(item.quantity, 2)
        self.assertEqual(item.pizza.name, "Pepperoni")
        self.assertEqual(self.cart.items.count(), 1)