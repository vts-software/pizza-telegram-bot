from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton("🍕 Меню", callback_data="menu")
    )

    keyboard.add(
        InlineKeyboardButton("🛒 Корзина", callback_data="cart")
    )

    keyboard.add(
        InlineKeyboardButton("📦 Мои заказы", callback_data="orders")
    )

    return keyboard


def pizza_keyboard(pizzas):

    keyboard = InlineKeyboardMarkup()

    for pizza in pizzas:

        keyboard.add(
            InlineKeyboardButton(
                f"{pizza.name} {pizza.size} — {pizza.price}",
                callback_data=f"pizza_{pizza.id}"
            )
        )

    return keyboard