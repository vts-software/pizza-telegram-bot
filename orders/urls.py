from django.urls import path
from .views import CheckoutView, all_orders_view


urlpatterns = [
    path("checkout/", CheckoutView.as_view()),
    path("", all_orders_view),
]