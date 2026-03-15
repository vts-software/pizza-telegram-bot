import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from tg_bot.telegram_bot import bot
import tg_bot.handlers