
from .models import Pizza
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response


@swagger_auto_schema(
    method="get",
    operation_description="Get list of pizzas"
)
@api_view(["GET"])
def pizza_list(request):

    pizzas = Pizza.objects.filter(available=True)

    data = []

    for pizza in pizzas:
        data.append({
            "id": pizza.id,
            "name": pizza.name,
            "size": pizza.size,
            "price": float(pizza.price)
        })

    return Response(data)