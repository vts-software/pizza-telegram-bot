from cart.models import Cart, CartItem
from orders.models import Order, OrderItem


def create_order_from_cart(user):

    cart, _ = Cart.objects.get_or_create(user=user)

    items = CartItem.objects.filter(cart=cart)

    if not items.exists():
        raise ValueError("Cart is empty")

    order = Order.objects.create(user=user)

    for item in items:

        OrderItem.objects.create(
            order=order,
            pizza=item.pizza,
            quantity=item.quantity,
            price=item.pizza.price
        )

    items.delete()

    return order