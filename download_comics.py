import requests
import random


def download_random_xkcd_comic():
    number_comics_url = 'https://xkcd.com/info.0.json'
    number_comics_response = requests.get(number_comics_url)
    number_comics_response.raise_for_status()
    last_comics_number = number_comics_response.json()['num']

    comics_url = f'https://xkcd.com/{random.randint(0, last_comics_number)}/info.0.json'
    response = requests.get(comics_url)
    response.raise_for_status()
    print(response.json()['alt'])
    comics_image_url = response.json()['img']

    comics_image_response = requests.get(comics_image_url)
    comics_image_response.raise_for_status()
    with open('comics.png', 'wb') as file:
        file.write(comics_image_response.content)