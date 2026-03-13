from .telegram_bot import bot
from .keyboards import main_menu

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


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    if call.data == "menu":

        pizzas = Pizza.objects.filter(available=True)

        text = "Наше меню 🍕\n\n"

        for pizza in pizzas:
            text += f"{pizza.id}. {pizza.name} {pizza.size} — {pizza.price}\n"

        bot.send_message(call.message.chat.id, text)

    elif call.data == "cart":

        user = TelegramUser.objects.get(
            telegram_id=call.from_user.id
        )

        items = CartItem.objects.filter(user=user)

        if not items:
            bot.send_message(call.message.chat.id, "Корзина пустая")
            return

        text = "Корзина 🛒\n\n"

        total = 0

        for item in items:
            text += f"{item.pizza.name} x{item.quantity}\n"
            total += item.pizza.price

        text += f"\nИтого: {total}"

        bot.send_message(call.message.chat.id, text)

    elif call.data == "orders":

        bot.send_message(call.message.chat.id, "Раздел заказов")