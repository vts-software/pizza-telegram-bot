from django.test import TestCase

from users.models import TelegramUser
from menu.models import Pizza
from cart.models import Cart, CartItem
from orders.models import Order, OrderItem


class OrderLogicTest(TestCase):

    def test_create_order_from_cart(self):

        user = TelegramUser.objects.create(
            telegram_id=999,
            first_name="BotUser"
        )

        cart = Cart.objects.create(user=user)

        pizza = Pizza.objects.create(
            name="Pepperoni",
            price=10,
            available=True
        )

        CartItem.objects.create(
            cart=cart,
            pizza=pizza,
            quantity=2
        )

        order = Order.objects.create(user=user)

        for item in cart.items.all():

            OrderItem.objects.create(
                order=order,
                pizza=item.pizza,
                quantity=item.quantity,
                price=item.pizza.price
            )

        cart.items.all().delete()

        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(cart.items.count(), 0)