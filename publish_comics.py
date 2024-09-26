import telegram
import os
from main import download_xkcd_comics
import time
import argparse


parser = argparse.ArgumentParser(description='Скачивает и публикует комиксы Xkcd про Python')
parser.add_argument('--delay_time', type=int, default=216000, help='Задержка между публикованием комиксов, По умолчанию - 1 час')
args = parser.parse_args()

while True:
    download_xkcd_comics()
    telegram_token = '7225530190:AAGVhABXHs1DBdKc8-v-hfs31Dtidkvxhog'
    bot = telegram.Bot(token=telegram_token)
    bot.send_document(chat_id='@xkcd_comicss', document=open('comics.png', 'rb'))
    os.remove("comics.png")
    time.sleep(args.delay_time)