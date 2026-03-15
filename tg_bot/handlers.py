from .telegram_bot import bot
from .keyboards import main_menu, pizza_keyboard, cart_keyboard

from menu.models import Pizza
from users.models import TelegramUser
from cart.models import Cart, CartItem
from orders.models import Order, OrderItem


def get_user(message):
    user, _ = TelegramUser.objects.get_or_create(
        telegram_id=message.from_user.id,
        defaults={
            "username": message.from_user.username,
            "first_name": message.from_user.first_name
        }
    )
    return user


# ---------------- START ---------------- #

@bot.message_handler(commands=['start'])
def start(message):

    get_user(message)

    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Pizza Bot 🍕",
        reply_markup=main_menu()
    )


# ---------------- MENU ---------------- #

@bot.message_handler(func=lambda message: message.text == "🍕 Меню")
def show_menu(message):

    pizzas = Pizza.objects.filter(available=True)

    bot.send_message(
        message.chat.id,
        "Выберите пиццу",
        reply_markup=pizza_keyboard(pizzas)
    )


# ---------------- ADD PIZZA ---------------- #

@bot.callback_query_handler(func=lambda call: call.data.startswith("pizza_"))
def add_to_cart(call):

    pizza_id = int(call.data.split("_")[1])
    pizza = Pizza.objects.get(id=pizza_id)

    user = TelegramUser.objects.get(
        telegram_id=call.from_user.id
    )

    cart, _ = Cart.objects.get_or_create(user=user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        pizza=pizza
    )

    if not created:
        item.quantity += 1
        item.save()

    bot.answer_callback_query(
        call.id,
        f"{pizza.name} добавлена в корзину 🛒"
    )


# ---------------- CART ---------------- #

@bot.message_handler(func=lambda message: message.text == "🛒 Корзина")
def show_cart(message):

    user = TelegramUser.objects.get(
        telegram_id=message.from_user.id
    )

    cart, _ = Cart.objects.get_or_create(user=user)
    items = CartItem.objects.filter(cart=cart)

    if not items:
        bot.send_message(message.chat.id, "Корзина пуста")
        return

    text = "🛒 Ваша корзина:\n\n"

    total = 0

    for item in items:

        price = item.pizza.price * item.quantity

        text += f"{item.pizza.name} x{item.quantity} — {price}\n"

        total += price

    text += f"\nИтого: {total}"

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=cart_keyboard(items)
    )


# ---------------- REMOVE ITEM ---------------- #

@bot.callback_query_handler(func=lambda call: call.data.startswith("remove_"))
def remove_from_cart(call):

    item_id = int(call.data.split("_")[1])

    item = CartItem.objects.get(id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        message = "Количество уменьшено 🛒"
    else:
        item.delete()
        message = "Пицца удалена из корзины 🗑"

    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        message
    )


# ---------------- CHECKOUT ---------------- #

@bot.callback_query_handler(func=lambda call: call.data == "checkout")
def create_order(call):

    user = TelegramUser.objects.get(
        telegram_id=call.from_user.id
    )

    cart, _ = Cart.objects.get_or_create(user=user)
    items = CartItem.objects.filter(cart=cart)

    if not items:
        bot.send_message(call.message.chat.id, "Корзина пуста")
        return

    order = Order.objects.create(user=user)

    total = 0

    for item in items:

        OrderItem.objects.create(
            order=order,
            pizza=item.pizza,
            quantity=item.quantity,
            price=item.pizza.price
        )

        total += item.pizza.price * item.quantity

    items.delete()

    bot.send_message(
        call.message.chat.id,
        f"Заказ #{order.id} успешно создан 🎉\nСумма: {total}"
    )


# ---------------- ORDERS ---------------- #

@bot.message_handler(func=lambda message: message.text == "📦 Мои заказы")
def show_orders(message):

    user = TelegramUser.objects.get(
        telegram_id=message.from_user.id
    )

    orders = Order.objects.filter(user=user)

    if not orders:
        bot.send_message(message.chat.id, "У вас пока нет заказов")
        return

    text = "📦 Ваши заказы:\n\n"

    for order in orders:

        total = sum(
            item.price * item.quantity
            for item in order.items.all()
        )

        text += f"Заказ #{order.id} — {total}\n"

    bot.send_message(message.chat.id, text)