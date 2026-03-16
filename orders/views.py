from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import TelegramUser
from .services import create_order_from_cart
from .models import Order



class CheckoutView(APIView):

    permission_classes = []

    def post(self, request):

        telegram_id = request.data.get("telegram_id")

        if not telegram_id:
            return Response(
                {"error": "telegram_id is required"},
                status=400
            )

        try:
            user = TelegramUser.objects.get(telegram_id=telegram_id)
        except TelegramUser.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=404
            )

        order = create_order_from_cart(user)

        return Response({
            "order_id": order.id,
            "status": order.status
        })
    

def all_orders_view(request):

    orders = Order.objects.all()

    data = []

    for order in orders:

        items = []
        total = 0

        for item in order.items.all():

            item_total = item.price * item.quantity

            items.append({
                "pizza": item.pizza.name,
                "price": float(item.price),
                "quantity": item.quantity,
                "total": float(item_total)
            })

            total += item_total

        data.append({
            "order_id": order.id,
            "user": order.user.telegram_id,
            "status": order.status,
            "items": items,
            "total_price": float(total)
        })

    return JsonResponse(data, safe=False)