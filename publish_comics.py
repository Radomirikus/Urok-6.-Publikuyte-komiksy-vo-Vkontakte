import telegram
import os
from download_comics import download_random_xkcd_comic
import time
import argparse
from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']

    while True:
        download_random_xkcd_comic()
        bot = telegram.Bot(token=telegram_token)
        try:
            bot.send_document(chat_id='@xkcd_comicss', document=open('comics.png', 'rb'))
            
        finally:
            os.remove("comics.png")

        time.sleep(5)


if __name__ == "__main__":
    main()