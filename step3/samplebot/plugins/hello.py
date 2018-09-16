# -*- coding: utf-8 -*-
# from slackbot.bot import respond_to
from slackbot.bot import respond_to, default_reply

# @default_reply
@respond_to('こんにちは')
def hello(message):
    message.reply('こんにちは')
    message.react('+1')

# @default_reply
# def reply_default_message(message):
#     message.reply('その言葉はわかりません')
