import telegram
import os
from download_comics import download_random_xkcd_comic
import time
import argparse
from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']

    download_random_xkcd_comic()
    bot = telegram.Bot(token=telegram_token)
    try:
        with open('comics.png', 'rb') as file:
            bot.send_document(chat_id='@xkcd_comicss', document=file)
        
    finally:
        os.remove("comics.png")


if __name__ == "__main__":
    main()