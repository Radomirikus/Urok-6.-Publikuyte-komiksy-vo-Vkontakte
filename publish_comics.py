import telegram
import os
from download_comics import download_random_xkcd_comic
import time
import argparse
from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']

    parser = argparse.ArgumentParser(description='Скачивает и публикует комиксы Xkcd про Python')
    parser.add_argument('--delay_time', type=int, default=216000, help='Задержка между публикованием комиксов, По умолчанию - 1 час')
    args = parser.parse_args()

    while True:
        download_random_xkcd_comic()
        bot = telegram.Bot(token=telegram_token)
        bot.send_document(chat_id='@xkcd_comicss', document=open('comics.png', 'rb'))
        os.remove("comics.png")
        time.sleep(args.delay_time)


if __name__ == "__main__":
    main()