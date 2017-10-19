#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.join(os.path.abspath('.'), 'lib'))

import telegram
from flask import Flask, request

app = Flask(__name__)

global bot
bot = telegram.Bot(token='291279465:AAGRvWtOS2VjhfIH_l-d5tn2EdXdTFZheo4')


@app.route('/HOOK', methods=['POST'])
def webhook_handler():
	if request.method == "POST":
		# retrieve the message in JSON and then transform it to Telegram object
		update = telegram.Update.de_json(request.get_json(force=True), bot)
		
		chat_id = update.message.chat.id
		
		# Telegram understands UTF-8, so encode text for unicode compatibility
		msg_text = update.message.text.encode('utf-8')
		
		#First row - Month and Year
		row=[[telegram.KeyboardButton(msg_text)]]
		#row.append(telegram.InlineKeyboardButton(msg_text,callback_data="ignore"))
		markup = telegram.ReplyKeyboardMarkup(row, one_time_keyboard=True)
		
		# repeat the same message back (echo)
		bot.sendMessage(chat_id=chat_id, text=msg_text, reply_markup=markup)
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
