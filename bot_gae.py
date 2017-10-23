#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.join(os.path.abspath('.'), 'lib'))

import telegram
from flask import Flask, request
from peewee import *


# --------- global constant section --------------


# --------- global variables ---------------------

start_button_list = [
    [telegram.KeyboardButton(u"Регистрация")]
]

app = Flask(__name__)

global bot
bot = telegram.Bot(token='291279465:AAGRvWtOS2VjhfIH_l-d5tn2EdXdTFZheo4')

# --------- functions ----------------------------

# universal function building menu with buttons
def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

@app.route('/HOOK', methods=['POST'])
def webhook_handler():
	#web hooks use only this type of request
	if request.method == "POST":
		# retrieve the message in JSON and then transform it to Telegram object
		update = telegram.Update.de_json(request.get_json(force=True), bot)

		chat_id = update.message.chat.id

		reply_text = u"Nothing to say"
		r_markup = None

		if update.message.text == "/start":
			r_markup = telegram.ReplyKeyboardMarkup(start_button_list,  resize_keyboard=True)
			reply_text = u"Please, go on trough registration in bot"

		if update.message.text == u"Регистрация":
			r_markup = None
			reply_text = u"Registration completed"

		# repeat the same message back (echo)
		bot.sendMessage(chat_id=chat_id, text=reply_text, reply_markup=r_markup)


	return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
	s = bot.setWebhook('https://botgamereg-hello.appspot.com/HOOK')
	if s:
		return "webhook setup ok"
	else:
		return "webhook setup failed"


@app.route('/')
def index():
	return '.'
