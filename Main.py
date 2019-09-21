# -*- coding: utf-8 -*-

import logging
from time import sleep

from telebot import TeleBot
from telebot.types import Message

import Support.Administration_Unit as Administration_Unit
import Support.Auxiliary_Unit as Auxiliary_Unit
import Support.Content_Block as Content_Block
from libs.Constant_Block import Log_Path, Log_Format, Token

logging.basicConfig(filename=Log_Path, level=logging.CRITICAL, filemode='w', format=Log_Format)
bot = TeleBot(Token)


@bot.message_handler(func=lambda Message: True, commands=['Menu'])
def Ad_1(message: Message):
    try:

        Administration_Unit.Menu_Command(bot, message)

    except Exception as Exc:

        logging.critical(Exc)


@bot.message_handler(func=lambda Message: True, commands=['GOOGLE'])
def Au_1(message: Message):
    try:

        Auxiliary_Unit.Search_Command(bot, message)

    except Exception as Exc:

        logging.critical(Exc)


@bot.message_handler(func=lambda Message: True, commands=[''])
def Command_Not_Found(message: Message):
    try:

        print('Other command')

    except Exception as Exc:

        logging.critical(Exc)


@bot.message_handler(content_types=['text'])
def text(message: Message):
    Content_Block.Text(bot, message)


@bot.message_handler(content_types=['audio', 'vidio', 'vidio_note', 'voice'])
def avnv(message: Message):
    Content_Block.AVNV(bot, message)


@bot.message_handler(content_types=['document'])
def doc(message: Message):
    Content_Block.Doc(bot, message)


@bot.message_handler(content_types=['photo'])
def photo(message: Message):
    Content_Block.Photo(bot, message)


@bot.message_handler(content_types=['sticker'])
def sticker(message: Message):
    Content_Block.Sticker(bot, message)


@bot.message_handler(content_types=['location', 'contact'])
def lc(message: Message):
    Content_Block.LC(bot, message)


@bot.message_handler(content_types=['new_chat_members'])
def ncm(message: Message):
    Content_Block.NCM(bot, message)


@bot.message_handler(content_types=['left_chat_member'])
def lcm(message: Message):
    Content_Block.LCM(bot, message)


@bot.message_handler(content_types=['new_chat_title'])
def nct(message: Message):
    Content_Block.NCT(bot, message)


for i in range(10):
    try:
        bot.polling(none_stop=True, timeout=60)

    except Exception:
        print(f'Restart attempt[{i}] ...')
        sleep(2)
