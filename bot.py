from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7068865201:AAFgK2W__UAtUzBMiudQ3HIOYlabCrJUVSE')


@bot.message_handler(commands=['start','help'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id,f"Assalomu Alaykum {full_name}")

@bot.message_handler(content_types=["text","photo","video"])
def get_text(message: Message):
    chat_id = message.chat.id
    # print(message.text)
    text = message.text
    # bot.send_message(chat_id, text)
    bot.copy_message(chat_id,chat_id,message.message_id)

bot.polling()