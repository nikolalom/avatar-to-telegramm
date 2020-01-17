"""
Сделано на основе поста https://habr.com/ru/post/457078/ (@mumtozvalijonov)

с моими небольшими доработками
"""
from telethon import TelegramClient, sync
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
import time
from config import *
from generate_time_images import *

client = TelegramClient('54664647864664', api_id, api_hash)
client.start()

while True:
    change_img()
    client(DeletePhotosRequest(client.get_profile_photos('me')))
    file = client.upload_file(f"time.png")
    client(UploadProfilePhotoRequest(file))
    time.sleep(30)

if __name__ == '__main__':
	pass
