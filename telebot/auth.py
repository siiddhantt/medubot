import requests
import json
from telebot.credentials import admin_email, admin_password
host = ""


def auth():
    headers = {'content-type': 'application/json'}
    data = {"email": admin_email, "password": admin_password}
    URL = host + "/admin/auth"
    res = requests.post(URL, data=json.dumps(data), headers=headers)
    cook = res.cookies.get_dict()["connect.sid"]
    with open('./telebot/credentials.py', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data[-1] = 'cookie = ' + '"' + cook + '"'
    with open('./telebot/credentials.py', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print(data)


auth()
