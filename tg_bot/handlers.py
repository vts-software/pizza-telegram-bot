from .telegram_bot import bot
from .keyboards import main_menu, pizza_keyboard

from menu.models import Pizza
from users.models import TelegramUser
from cart.models import CartItem


def get_user(message):

    user, _ = TelegramUser.objects.get_or_create(
        telegram_id=message.from_user.id,
        defaults={
            "username": message.from_user.username,
            "first_name": message.from_user.first_name
        }
    )

    return user


@bot.message_handler(commands=['start'])
def start(message):

    get_user(message)

    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Pizza Bot 🍕",
        reply_markup=main_menu()
    )


@bot.callback_query_handler(func=lambda call: call.data == "menu")
def show_menu(call):

    pizzas = Pizza.objects.filter(available=True)

    bot.send_message(
        call.message.chat.id,
        "Выберите пиццу 🍕",
        reply_markup=pizza_keyboard(pizzas)
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("pizza_"))
def add_to_cart(call):

    pizza_id = int(call.data.split("_")[1])

    pizza = Pizza.objects.get(id=pizza_id)

    user = TelegramUser.objects.get(
        telegram_id=call.from_user.id
    )

    CartItem.objects.create(
        user=user,
        pizza=pizza,
        quantity=1
    )

    bot.send_message(
        call.message.chat.id,
        f"{pizza.name} добавлена в корзину 🛒"
    )