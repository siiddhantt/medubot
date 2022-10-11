import requests
from telebot.credentials import cookie
host = ""


def getProducts():
    URL = host + "/store/products"
    r = requests.get(url=URL)
    data = r.json()
    title = data["products"]
    return title


def getProduct(pid):
    URL = host + "/store/products/" + pid
    r = requests.get(url=URL)
    data = r.json()
    return data


def getOrders():
    cook = {'connect.sid': cookie}
    URL = host + "/admin/orders"
    r = requests.get(url=URL, cookies=cook)
    data = r.json()
    title = data["orders"]
    return title
