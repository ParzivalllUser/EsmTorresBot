# -*- coding: utf-8 -*-

from Response import Response_Block
from libs import Constant_Block
from libs.Auxiliary import Message_From_Admin


def Text(bot, message):
    if (message.chat.type in Constant_Block.Type_Groups and Constant_Block.Text) or Message_From_Admin(bot, message):
        pass

    else:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)

    del message


def AVNV(bot, message):
    if (message.chat.type in Constant_Block.Type_Groups and Constant_Block.AVNV) or Message_From_Admin(bot, message):
        pass

    else:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)

    del message


def Doc(bot, message):
    if (message.chat.type in Constant_Block.Type_Groups and Constant_Block.Doc) or Message_From_Admin(bot, message):
        pass

    else:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)

    del message


def Photo(bot, message):
    if (message.chat.type in Constant_Block.Type_Groups and Constant_Block.Photo) or Message_From_Admin(bot, message):
        pass

    else:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)

    del message


def Sticker(bot, message):
    if (message.chat.type in Constant_Block.Type_Groups and Constant_Block.Sticker) or Message_From_Admin(bot, message):
        pass

    else:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)

    del message


def LC(bot, message):
    if (message.chat.type in Constant_Block.Type_Groups and Constant_Block.LC) or Message_From_Admin(bot, message):
        pass

    else:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)

    del message


def NCM(bot, message):
    if Constant_Block.NCM and message.chat.type in Constant_Block.Type_Groups:
        # Response_Block.Deleter(bot, message.chat.id, message.message_id)
        Response_Block.NCM(bot, message.chat.id, message.chat.title, message.from_user.language_code)

    else:
        pass

    del message


def LCM(bot, message):
    if Constant_Block.LCM and message.chat.type in Constant_Block.Type_Groups:
        Response_Block.Deleter(bot, message.chat.id, message.message_id)

    else:
        pass

    del message


def NCT(bot, message):
    if Constant_Block.NCT and message.chat.type in Constant_Block.Type_Groups:
        Response_Block.NCT(bot, message.chat.id)

    else:
        pass

    del message
