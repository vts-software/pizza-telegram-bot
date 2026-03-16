from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from cart.models import CartItem, Cart
from users.models import TelegramUser


@swagger_auto_schema(
    method="get",
    operation_description="Get user cart by telegram id"
)
@api_view(["GET"])
def cart_view(request, telegram_id):

    try:
        user = TelegramUser.objects.get(
            telegram_id=telegram_id
        )

    except TelegramUser.DoesNotExist:

        return Response(
            {"error": "User not found"},
            status=404
        )

    cart = Cart.objects.filter(user=user).first()

    if not cart:

        return Response({
            "user": user.telegram_id,
            "items": [],
            "total_price": 0
        })

    items = CartItem.objects.filter(cart=cart)

    cart_items = []
    total_price = 0

    for item in items:

        pizza = item.pizza
        item_total = pizza.price * item.quantity

        cart_items.append({
            "pizza_id": pizza.id,
            "name": pizza.name,
            "size": pizza.size,
            "price": float(pizza.price),
            "quantity": item.quantity,
            "total": float(item_total)
        })

        total_price += item_total

    return Response({
        "user": user.telegram_id,
        "items": cart_items,
        "total_price": float(total_price)
    })