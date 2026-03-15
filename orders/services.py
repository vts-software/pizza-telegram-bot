from cart.models import Cart
from orders.models import Order, OrderItem


def create_order_from_cart(user):

    cart = Cart.objects.get(user=user)

    order = Order.objects.create(user=user)

    for item in cart.items.all():

        OrderItem.objects.create(
            order=order,
            pizza=item.pizza,
            quantity=item.quantity,
            price=item.pizza.price
        )

    cart.items.all().delete()

    return order