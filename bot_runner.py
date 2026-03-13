import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from bot.bot import bot
import bot.handlers

bot.infinity_polling()