import os
import requests
from bs4 import BeautifulSoup
import cloudinary.uploader

CLOUDINARY_KEY = os.environ['CLOUDINARY_API_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_API_SECRET']
CLOUDINARY_CLOUD = os.environ['CLOUDINARY_CLOUD_NAME']

def get_speakerdeck_thumbnail(speakerdeck_url):
    page = requests.get(speakerdeck_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    deck_bg_style = soup.find_all('div', class_='deck-background')[0].get('style')
    deck_bg_img = deck_bg_style.split('(')[1][1:-2]
    result = cloudinary.uploader.upload(deck_bg_img, 
                                    api_key=CLOUDINARY_KEY,
                                    api_secret=CLOUDINARY_SECRET, 
                                    cloud_name=CLOUDINARY_CLOUD)
    return result['secure_url']