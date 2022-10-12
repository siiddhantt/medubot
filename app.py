from telebot.apis import *
from telebot.credentials import bot_token, bot_user_name, URL, cookie
import re
from flask import Flask, request
import telegram
import importlib
import telebot.credentials
importlib.reload(telebot.credentials)


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
                if len(products) == 0:
                    s = "No products!"
                for p in products:
                    s += "ID: `%s`\nName: *%s*\nDescription: %s\n" % (
                        p["id"], p["title"], p["description"])
                    s += "\n"
                bot.sendMessage(chat_id=chat_id, text=s, parse_mode="Markdown",
                                reply_to_message_id=msg_id)
            elif text == "/orders":
                s = ""
                orders = getOrders()
                if len(orders) == 0:
                    s = "No orders!"
                for o in orders:
                    s += "ID: `%s`\nSubtotal: %s\nPaid Total: %s\nStatus: %s\nPayment Status: %s\n" % (
                        o["id"], o["subtotal"], o["paid_total"], o["status"], o["payment_status"])
                    s += "\n"
                bot.sendMessage(chat_id=chat_id, text=s, parse_mode="Markdown",
                                reply_to_message_id=msg_id)
            elif text[0:9] == "/product " and len(text) > 9:
                pid = text[9:]
                s = ""
                p = getProduct(pid)
                if "product" in p:
                    p = p["product"]
                    s = "ID: %s\n\nName: %s\n\nDescription: %s\n" % (
                        p["id"], p["title"], p["description"])
                    url = p["thumbnail"]
                    bot.sendPhoto(chat_id=chat_id, caption=s, photo=url,
                                  reply_to_message_id=msg_id)
                else:
                    s = "No product with that product-ID found!"
                    bot.sendMessage(chat_id=chat_id, text=s,
                                    reply_to_message_id=msg_id)
            elif text == "/auth":
                import telebot.auth
                telebot.auth
                print(cookie)
        except Exception:
            # if things went wrong
            bot.sendMessage(
                chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = True
    s = bot.setWebhook('{URL}{HOOK}'.format(
        URL=URL, HOOK=TOKEN), drop_pending_updates=True)
    if s:
        return "Webhook setup successful!"
    else:
        return "Webhook setup failed."


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
