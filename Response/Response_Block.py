# -*- coding: utf-8 -*-

from telebot import apihelper

from libs.Constant_Block import Default_Language


def Deleter(bot, chat_id, message_id):
    try:
        bot.delete_message(chat_id, message_id)

    except apihelper.ApiException:
        pass


def NCM(bot, chat_id, title, language):
    try:
        if Default_Language in language:
            bot.send_message(chat_id, f'Добро пожаловать в группу - {title}, будь как дома.')

        else:
            bot.send_message(chat_id, f'Welcome to band - {title}, make yourself at home.')

    except apihelper.ApiException:
        pass


def NCT(bot, chat_id):
    try:
        bot.send_message(chat_id, f'[{Default_Language.title()}]Новое название - всегда лучше старого.\n\
        [En]A new name is always better than an old one.')

    except apihelper.ApiException:
        pass


def Error_NoAllowed(bot, user_id, language):
    try:
        if Default_Language in language:
            bot.send_message(user_id, f'[{language.title()}]Ошибка!\nОграничена возможность отправки команд.')

        else:
            bot.send_message(user_id, '[En]Error!\nThe ability to send commands is limited.')

    except apihelper.ApiException:
        pass


def Warn(bot, message, User_Status, main_id):
    Answer = f'From user: \n' \
             f'  Id: {message.from_user.id},\n' \
             f'  Username: @{message.from_user.username},\n' \
             f'  Status: {User_Status[0]};\n' \
             f'To user: \n' \
             f'  Id: {message.reply_to_message.from_user.id},\n' \
             f'  Username: @{message.reply_to_message.from_user.username},\n' \
             f'  Status: {User_Status[1]};\n' \
             f'Chat: \n' \
             f'  Id: {message.reply_to_message.chat.id},\n' \
             f'  Title: {message.reply_to_message.chat.title},\n' \
             f'  Text: {message.reply_to_message.text}.'

    Deleter(bot, message.chat.id, message.message_id)
    bot.send_message(main_id, Answer)
