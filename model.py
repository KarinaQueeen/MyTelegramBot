from aiogram import types
from controller import dp
from aiogram.dispatcher import Dispatcher
from keyboards.client_kb import keyboard


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=keyboard)


@dp.message_handler(commands=['ДвоичнаяCистема'])
async def translate(message: types.Message):
    await message.answer(f'Какое число переведем?')
    transl()


@dp.message_handler(commands=['Зашифровать'])
async def coding(message: types.Message):
    await message.answer('Напиши что-нибудь:')
    cod()


@dp.message_handler(commands=['Расшифровать'])
async def decoding(message: types.Message):
    await message.answer(f'Укажи строку:')
    decod()


@dp.message_handler(content_types=['text'])
async def transl(message: types.Message):
    num = int(message.text)
    new_list = []
    while num:
        new_list.append(num % 2)
        num //= 2
    result = ''
    for el in new_list[::-1]:
        result += str(el)
    await message.answer(result)


@dp.message_handler(content_types=['text'])
async def cod(message: types.Message):
    print(message.text)
    # code = ''
    # count = 1
    # symbol = ''
    # for s in message.text:
    #    if s != symbol:
    #        if symbol:
    #            code += str(count) + symbol
    #            count = 1
    #            symbol = s
    #        else:
    #            if count == 9:
    #                code += str(count) + symbol
    #                count = 1
    #            count += 1
    #     # result = code
    # await message.answer(result)


@dp.message_handler(content_types=['text'])
async def decod(message: types.Message):
    print(message.text)
    # def decoding(code):
    #    decode = ''
    #    for i in range(0, len(code), 2):
    #        count, simbol = code[i: i + 1]
    #        decode += simbol * int(count)
    #    return decode
    # await message.answer(result)


def register_message(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(translate, commands=['Двоичная система'])
    dp.register_message_handler(coding, commands=['Зашифровать'])
    dp.register_message_handler(decoding, commands=['Расшифровать'])
