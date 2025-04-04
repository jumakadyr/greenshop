# import telebot
#
# from .models import Checkout
#
# bot_token = '7311392605:AAEM6TYmIXrPZw6My6so-Zdn0BXM5WXsFxY'
# chat_id = '1444648081'
#
#
# def send_checkout(instance):
#     instance = Checkout.objects.all()
#     bot = telebot.TeleBot(bot_token)
#     message_text = (f"ФИО: {instance.first_name}\n"
#                 f"Номер: {number}\n"
#                 f"Текст отзыва: {text}")
#
#     bot.send_message(chat_id, message_text)