# MeduBot

<img width="1600" alt="MeduBotCover" src="https://user-images.githubusercontent.com/47355538/195445061-2a6ab2eb-14a4-42b0-aa1b-1896ffe3527b.png">

## About

### Participants

Siddhant Rai - ![siiddhantt](https://github.com/siiddhantt) - wh1tew0lf#2953 (Discord)

Prashant Singh - ![PrashantS360](https://github.com/prashants360)

### Description

MeduBot provides an integration between your Medusajs-based backend/store and Telegram. It is a python implementation to use a telegram bot 
as a store-manager/admin.

#### Backend
```
https://github.com/siiddhantt/digimart-medusa-backend
```
#### Backend-Deployed
```
https://digimart-medusa-backend.herokuapp.com
```

### Preview

A sample bot is hosted on Heroku with it's username on telegram being @medusajs_bot.

https://user-images.githubusercontent.com/47355538/195455427-6baa4f55-ca4a-4f51-aa49-d33017fafa18.mp4

## Features

- Easily link your Medusa server by addng it's url in the host field
- Add new APIs to extend further upon the current build
- Functions to get products, orders, product by ID, order by ID, etc
- Auth endpoint to automatically authorise the admin

## Set up Project

### Prerequisites
Before you start with the tutorial make sure you have

- [Python](https://www.python.org) v3.0 or greater
- [Medusa Server](https://docs.medusajs.com/quickstart/quick-start/) hosted on a cloud platform

### Install Project

1. Clone the repository:

```bash
git clone https://github.com/siiddhantt/medubot
```

2. Edit the 'credentials.py' file in telebot and add the values to the corresponding fields.

![image](https://user-images.githubusercontent.com/47355538/195454526-a7dc72ce-d428-4a8a-a19d-26ee3ebf86d2.png)

3.  Host the bot on cloud platform like Heroku

4. Start using your bot by seaching the bot's username in telegram and typing /start

## Resources
- [Medusa’s GitHub repository](https://github.com/medusajs/medusa)
- [Medusa Admin Panel](https://github.com/medusajs/admin)
- [Medusa Documentation](https://docs.medusajs.com/)

