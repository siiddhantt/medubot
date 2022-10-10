import requests

host = ""


def getProducts():
    URL = host + "/store/products"
    r = requests.get(url = URL)
    data = r.json()
    title = data["products"]
    return title