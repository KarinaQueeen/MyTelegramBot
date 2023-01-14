from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key1 = KeyboardButton('/ДвоичнаяCистема')
key2 = KeyboardButton('/Зашифровать')
key3 = KeyboardButton('/Расшифровать')

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(key1).add(key2).add(key3)
