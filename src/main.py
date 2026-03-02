import os
from dotenv import load_dotenv

import telebot
from telebot import types

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

if __name__ == "__main__":
    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,'Привет')

    @bot.message_handler(commands=['button'])
    def button_message(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Кнопка")
        markup.add(item1)
    
    bot.infinity_polling()