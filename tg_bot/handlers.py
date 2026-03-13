from .telegram_bot import bot
from .keyboards import main_menu


@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Pizza Bot 🍕",
        reply_markup=main_menu()
    )


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    if call.data == "menu":
        bot.send_message(call.message.chat.id, "Вот наше меню 🍕")

    elif call.data == "cart":
        bot.send_message(call.message.chat.id, "Ваша корзина 🛒")

    elif call.data == "orders":
        bot.send_message(call.message.chat.id, "Ваши заказы 📦")