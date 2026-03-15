from .telegram_bot import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .keyboards import main_menu, pizza_keyboard, cart_keyboard

from menu.models import Pizza
from users.models import TelegramUser
from cart.models import CartItem
from orders.models import Order


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
        "Выберите пиццу",
        reply_markup=pizza_keyboard(pizzas)
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("pizza_"))
def add_to_cart(call):

    pizza_id = int(call.data.split("_")[1])

    pizza = Pizza.objects.get(id=pizza_id)

    user = TelegramUser.objects.get(
        telegram_id=call.from_user.id
    )

    item, created = CartItem.objects.get_or_create(
        user=user,
        pizza=pizza
    )

    if not created:
        item.quantity += 1
        item.save()

    bot.send_message(
        call.message.chat.id,
        f"{pizza.name} добавлена в корзину 🛒"
    )


@bot.callback_query_handler(func=lambda call: call.data == "cart")
def show_cart(call):

    user = TelegramUser.objects.get(
        telegram_id=call.from_user.id
    )

    items = CartItem.objects.filter(user=user)

    if not items:
        bot.send_message(call.message.chat.id, "Корзина пуста")
        return

    text = "🛒 Ваша корзина:\n\n"

    total = 0

    for item in items:

        price = item.pizza.price * item.quantity

        text += f"{item.pizza.name} x{item.quantity} — {price}\n"

        total += price

    text += f"\nИтого: {total}"

    bot.send_message(
        call.message.chat.id,
        text,
        reply_markup=cart_keyboard(items)
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("remove_"))
def remove_from_cart(call):

    item_id = int(call.data.split("_")[1])

    CartItem.objects.filter(id=item_id).delete()

    bot.send_message(
        call.message.chat.id,
        "Товар удалён из корзины"
    )


@bot.callback_query_handler(func=lambda call: call.data == "checkout")
def confirm_order(call):

    user = TelegramUser.objects.get(
        telegram_id=call.from_user.id
    )

    items = CartItem.objects.filter(user=user)

    if not items:
        bot.send_message(call.message.chat.id, "Корзина пуста")
        return

    total = 0

    text = "Подтвердите заказ:\n\n"

    for item in items:

        price = item.pizza.price * item.quantity

        text += f"{item.pizza.name} x{item.quantity} — {price}\n"

        total += price

    text += f"\n Итого: {total}"

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            "✅ Подтвердить",
            callback_data="confirm_order"
        )
    )

    bot.send_message(
        call.message.chat.id,
        text,
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data == "confirm_order")
def create_order(call):

    user = TelegramUser.objects.get(
        telegram_id=call.from_user.id
    )

    items = CartItem.objects.filter(user=user)

    total = 0

    for item in items:
        total += item.pizza.price * item.quantity

    order = Order.objects.create(
        user=user,
        total_price=total
    )

    items.delete()

    bot.send_message(
        call.message.chat.id,
        f"Заказ #{order.id} успешно создан 🎉"
    )


@bot.callback_query_handler(func=lambda call: call.data == "orders")
def show_orders(call):

    user = TelegramUser.objects.get(
        telegram_id=call.from_user.id
    )

    orders = Order.objects.filter(user=user)

    if not orders:
        bot.send_message(call.message.chat.id, "У вас пока нет заказов")
        return

    text = "📦 Ваши заказы:\n\n"

    for order in orders:
        text += f"Заказ #{order.id} — {order.total_price}\n"

    bot.send_message(call.message.chat.id, text)