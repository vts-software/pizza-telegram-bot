from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def main_menu():

    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.row(
        KeyboardButton("🍕 Меню"),
        KeyboardButton("🛒 Корзина")
    )

    keyboard.row(
        KeyboardButton("📦 Мои заказы")
    )

    return keyboard


def pizza_keyboard(pizzas):

    keyboard = InlineKeyboardMarkup()

    for pizza in pizzas:

        keyboard.add(
            InlineKeyboardButton(
                f"🍕 {pizza.name} ({pizza.size}) — {pizza.price}",
                callback_data=f"pizza_{pizza.id}"
            )
        )

    return keyboard


def cart_keyboard(items):

    keyboard = InlineKeyboardMarkup()

    for item in items:

        keyboard.row(
            InlineKeyboardButton(
                f"➖ {item.pizza.name}",
                callback_data=f"remove_{item.id}"
            ),
            InlineKeyboardButton(
                f"➕ {item.pizza.name}",
                callback_data=f"pizza_{item.pizza.id}"
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            "✅ Оформить заказ",
            callback_data="checkout"
        )
    )

    return keyboard