import os
from bot_app import bot


def main():
    print("🍕 Pizza Bot is starting...")
    print(f"🤖 PID: {os.getpid()}")
    print("🚀 Polling started...\n")

    bot.infinity_polling()


if __name__ == "__main__":
    main()