from django.http import JsonResponse
from .models import Pizza


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

    return JsonResponse(data, safe=False)