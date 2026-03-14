from django.test import TestCase
from .models import Pizza


class PizzaModelTest(TestCase):

    def setUp(self):

        self.pizza = Pizza.objects.create(
            name="Pepperoni",
            description="Classic pizza",
            size="M",
            price=15,
            available=True
        )

    def test_pizza_created(self):

        self.assertEqual(self.pizza.name, "Pepperoni")

    def test_pizza_price(self):

        self.assertEqual(self.pizza.price, 15)

    def test_pizza_available(self):

        self.assertTrue(self.pizza.available)