# -*- coding: utf-8 -*-

import re
import urllib.parse

from Response import Response_Block
from libs import Constant_Block
from libs.Auxiliary import Message_From_Admin
from libs.Constant_Block import Search_Allowed


def Search_Command(bot, message):
    if (Search_Allowed or Message_From_Admin(bot, message)) and message.chat.type in Constant_Block.Search:
        pattern = re.compile(r'[\w\s+-=?!]+', re.UNICODE)
        result = pattern.findall(message.text, pos=8)

        string = ''
        for i in result:
            string += i

        string = re.sub(r'\s+', r' ', string)
        string = re.sub(r'\++', r'+', string)
        string = re.sub(r'\-+', r'-', string)
        string = re.sub(r'\?+', r'?', string)
        string = re.sub(r'\!+', r'!', string)

        query = urllib.parse.urlencode({'q': string}, encoding='cp1251')
        url = f'https://www.google.ru/search?{query}'

        bot.send_message(message.chat.id, url)

    elif message.chat.type not in Constant_Block.Search:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)
        Response_Block.Error_NoAllowed(bot, message.from_user.id, message.from_user.language_code)

    else:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)

    del message

# def Warn_Command(bot, message: Message):
#     if (Warn_Allowed() and message.chat.type in Constant_Block.Type_Groups):
#
#         if message.chat.id == Constant_Block.MainID:
#             return Response_Block.Deleter(bot, message.chat.id, message.message_id)
#
#         User_Status = []
#
#         if Message_From_Admin(bot, message):
#             User_Status.append('Администратор / Administration')
#
#         else:
#             User_Status.append('Пользователь / User')
#
#         if Message_From_Admin(bot, message.reply_to_message):
#             User_Status.append('Администратор / Administration')
#
#         else:
#             User_Status.append('Пользователь / User')
#
#         Response_Block.Warn(bot, message, User_Status, Constant_Block.MainID)
#
#     else:
#         Response_Block.Deleter(bot, message.chat.id, message.message_id)
#
#     del message
