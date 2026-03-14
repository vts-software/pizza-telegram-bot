from django.urls import path
from .views import cart_view

urlpatterns = [
    path("<int:telegram_id>/", cart_view),
]