"""API requests to external Slideshare API"""
import requests
import os
import hashlib
import time

API_KEY = os.getenv('API_KEY')
SHARED_SECRET = os.getenv('SHARED_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

TIMESTAMP = str(int(time.time()))
hash = hashlib.sha1((SHARED_SECRET + TIMESTAMP).encode()).hexdigest()

def api_request(tag_name):
    url = "https://www.slideshare.net/api/2/get_slideshows_by_tag"
    tag = tag_name
    limit = 10
    url_string = f"{url}?tag={tag}&limit={limit}&api_key={API_KEY}&hash={hash}&ts={TIMESTAMP}"
    print(url_string)
    response = requests.get(url_string)
    if response.status_code == 200:
        return response.text
    return False