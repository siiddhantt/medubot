import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name, URL
from telebot.apis import *


global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    # for debugging purposes only
    print("got text message :", text)
    # the first time you chat with the bot AKA the welcoming message
    if text == "/start":
        # print the welcoming message
        bot_welcome = """
       Welcome to MeduBot, this bot can be used to manage the inventory of your Medusa-based e-commerce store."""
        # send the welcoming message
        bot.sendMessage(chat_id=chat_id, text=bot_welcome,
                        reply_to_message_id=msg_id)

    else:
        try:
            if text == "/products":
                s = ""
                products = getProducts()
                for p in products:
                    s += "Name: %s\nID: %s\nDescription: %s\n" % (
                        p["title"], p["id"], p["description"])
                    s += "\n"
                bot.sendMessage(chat_id=chat_id, text=s,
                                reply_to_message_id=msg_id)
            # bot.sendPhoto(chat_id=chat_id, photo=url,
            #               reply_to_message_id=msg_id)
        except Exception:
            # if things went wrong
            bot.sendMessage(
                chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "Webhook setup successful!"
    else:
        return "Webhook setup failed."


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
