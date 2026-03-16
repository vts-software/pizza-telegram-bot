from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from users.models import TelegramUser
from .services import create_order_from_cart
from .models import Order


class CheckoutView(APIView):

    @swagger_auto_schema(
        operation_description="Create order from user's cart",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["telegram_id"],
            properties={
                "telegram_id": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Telegram user id"
                )
            }
        )
    )
    def post(self, request):

        telegram_id = request.data.get("telegram_id")

        if not telegram_id:
            return Response(
                {"error": "telegram_id is required"},
                status=400
            )

        try:
            user = TelegramUser.objects.get(
                telegram_id=telegram_id
            )

        except TelegramUser.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=404
            )

        try:
            order = create_order_from_cart(user)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=400
            )

        return Response({
            "order_id": order.id,
            "status": order.status
        })


@swagger_auto_schema(
    method="get",
    operation_description="Get all orders in the system"
)
@api_view(["GET"])
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

    return Response(data)