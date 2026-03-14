from django.http import JsonResponse
from cart.models import CartItem
from users.models import TelegramUser


def cart_view(request, telegram_id):

    try:
        user = TelegramUser.objects.get(telegram_id=telegram_id)
    except TelegramUser.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"},
            status=404
        )

    items = CartItem.objects.filter(user=user)

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

    data = {
        "user": user.telegram_id,
        "items": cart_items,
        "total_price": float(total_price)
    }

    return JsonResponse(data)