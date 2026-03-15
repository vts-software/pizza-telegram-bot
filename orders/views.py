from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import create_order_from_cart


class CheckoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        order = create_order_from_cart(request.user)

        return Response({
            "order_id": order.id,
            "status": order.status
        })