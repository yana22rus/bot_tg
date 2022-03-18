#!/usr/bin/env python3

from time import sleep
from os import getcwd, listdir
from datetime import datetime
from random import randrange
import telebot


def random_files(type):
    files = listdir(f"{getcwd()}/{type}")
    index = randrange(0, len(files))

    with open(f"{type}/{files[index]}", 'rb') as f:
        image_bytes = f.read()

    return image_bytes


def save_id_user(id_user):
    with open("id.txt") as f:
        db = f.readlines()

    id_user = f"{id_user}{chr(10)}"

    if id_user not in db:
        with open("id.txt", "a") as f:
            f.writelines(id_user)


bot = telebot.TeleBot('1950425331:AAGEpY9tH8SgS7oy2sWn-V05A9tWWv8D4w0')


@bot.message_handler(commands=['Photo', 'photo', 'Фото', 'фото', 'фотки'])
def dow_photo(message):
    try:

        save_id_user(message.from_user.id)
        bot.send_message(message.chat.id, "Для загрузки нового изображения напиши /photo")
        bot.send_photo(message.chat.id, random_files("photo"))
        save_id_user(message.from_user.id)

    except Exception:

        print(f"Упал {datetime.now().strftime('%m/%d/%y %H:%M:%S')}")

        sleep(5)


@bot.message_handler(commands=["Gif", "gif", "Гиф", "гиф", "Гифки", "гифки"])
def dow_gif(message):
    try:

        save_id_user(message.from_user.id)
        bot.send_message(message.chat.id, "Для загрузки нового гифки напиши /gif")
        bot.send_video(message.chat.id, random_files("gif"))


    except Exception:

        print(f"Упал {datetime.now().strftime('%m/%d/%y %H:%M:%S')}")

        sleep(5)


@bot.message_handler(commands=['push'])
def start_message(message):
    with open("id.txt") as f:

        db = f.readlines()

    for x in range(len(db)):

        try:

            bot.send_photo(db[x], photo=open('img.jpg', 'rb'), caption="У бота новые фотки /start")
            print(x)
        except Exception:
            pass


@bot.message_handler(commands=['zzz'])
def zzz(message):
    print(bot.send_message(message.chat.id, message.from_user.id))


@bot.message_handler(commands=['push_video'])
def push_video(message):
    with open("id.txt") as f:

        db = f.readlines()

    for x in range(len(db)):

        try:

            bot.send_video(db[x], video=open('video.mp4', 'rb'), caption="У бота новые опции /start")

            print(x)
        except Exception:
            pass


@bot.message_handler(commands=["Start", "start", "Старт", "старт"])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_photo = telebot.types.KeyboardButton("/Photo")
    button_gif = telebot.types.KeyboardButton("/Gif")
    markup.add(button_photo, button_gif)
    save_id_user(message.from_user.id)
    bot.send_message(message.chat.id, "Выберете команду", reply_markup=markup)


bot.polling(none_stop=True)

