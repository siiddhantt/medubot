import requests

host = ""

def getProducts():
    URL = host + "/store/products"
    r = requests.get(url = URL)
    data = r.json()
    title = data["products"]
    return title

def getOrders():
    cookie = {'connect.sid': 's%3Aa3iMHZk03QwSW6eSDYHR813XdidRpc06.gvO0cjCTakU8buuHVeoVQxsWZbfjwBDX9djtMsfrAhc'}
    URL = host + "/admin/orders"
    r = requests.get(url = URL,cookies=cookie)
    data = r.json()
    title = data["orders"]
    return data