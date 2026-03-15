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
                f"{pizza.name} {pizza.price}",
                callback_data=f"pizza_{pizza.id}"
            )
        )

    return keyboard


def cart_keyboard(items):

    keyboard = InlineKeyboardMarkup()

    for item in items:

        keyboard.add(
            InlineKeyboardButton(
                f"❌ удалить {item.pizza.name}",
                callback_data=f"remove_{item.id}"
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            "✅ Оформить заказ",
            callback_data="checkout"
        )
    )

    return keyboard