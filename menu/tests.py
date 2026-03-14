from django.test import TestCase
from faker import Faker
from .models import Pizza

fake = Faker()


class PizzaFakerTest(TestCase):

    def test_create_random_pizza(self):

        pizza = Pizza.objects.create(
            name=fake.word(),
            description=fake.text(),
            size="M",
            price=10,
            available=True
        )

        self.assertTrue(pizza.available)