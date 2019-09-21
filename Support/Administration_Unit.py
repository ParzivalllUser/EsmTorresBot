# -*- coding: utf-8 -*-

from telebot import apihelper

from Response import Response_Block
from libs import Constant_Block
from libs.Auxiliary import Message_From_Admin
from libs.Constant_Block import Menu_Allowed


def Menu_Command(bot, message):
    if (Menu_Allowed and Message_From_Admin(bot, message)) and message.chat.type in Constant_Block.Menu:

        try:
            bot.send_message(message.chat.id, 'Извените, находится в разработке')

        except apihelper.ApiException:
            pass

    elif message.chat.type not in Constant_Block.Menu:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)
        Response_Block.Error_NoAllowed(bot, message.from_user.id, message.from_user.language_code)

    else:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)

    del message

# def Dump_Command(message: Message):
#     if Constant_Block.COMmode and bot.get_chat_member(MainID,
#                                                       message.from_user.id).status in Constant_Block.Type_Admins:
#
#         if message.chat.type == Constant_Block.Type_Private or message.chat.id == MainID:
#
#             SE = re.search(r'"(\S|\W)*"', message.text)
#
#             if SE:
#
#                 SE = re.split(r',', SE.group())
#
#                 if '"All"' in SE:
#
#                     for i in Constant_Block.DU_list:
#
#                         Path = f'{os.getcwd()}\\{Constant_Block.DU_list.get(i)}'
#
#                         if os.path.exists(Path):
#
#                             Response_Block.Dump(bot, message.chat.id, Path, i, message.from_user.language_code)
#
#                         else:
#
#                             Response_Block.DumpERR_1(bot, message.chat.id, message.from_user.language_code, i)
#
#                 else:
#
#                     for i in SE:
#
#                         i = re.sub(r'^(\s)|(\s)$', '', i)
#                         SE = re.sub(r'^(\s+|")|(\s|")$', '', i)
#
#                         Path = f'{os.getcwd()}\\{Constant_Block.DU_list.get(SE)}'
#
#                         if SE in Constant_Block.DU_list and os.path.exists(Path):
#
#                             Response_Block.Dump(bot, message.chat.id, Path, SE, message.from_user.language_code)
#
#                         else:
#
#                             Response_Block.DumpERR_1(bot, message.chat.id, message.from_user.language_code, SE)
#
#             else:
#
#                 Response_Block.DumpERR_2(bot, message.chat.id, message.from_user.language_code)
#
#         else:
#
#             Response_Block.Deleter(bot, message.chat.id, message.message_id)
#
#     else:
#
#         Response_Block.Problem(bot, message.from_user.id, message.from_user.language_code)
#         Response_Block.Deleter(bot, message.chat.id, message.message_id)
#
#     del message
