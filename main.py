from telebot import TeleBot, types  # библиотека для работы бота, общения, обработки сообщений и библиотека дл реализации кнопок
import os

token = os.getenv('TOKEN')  # импортируем токен из файла .env и присваиваем переменной, для дальнейшего использования

bot = TeleBot(token, parse_mode=None)  # инициализация бота