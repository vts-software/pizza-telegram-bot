from django.test import TestCase
from .models import Pizza


class PizzaTest(TestCase):

    def test_create_pizza(self):

        pizza = Pizza.objects.create(
            name="Pepperoni",
            description="Classic",
            size="M",
            price=15
        )

        self.assertEqual(pizza.name, "Pepperoni")