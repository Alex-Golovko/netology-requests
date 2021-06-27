import requests
from yadisk import YandexDisk

TOKEN = 'AQAAAAAWwSZPAADLW55Sy2uaJEbAlEL1Ms0UfJA'

ya = YandexDisk(token=TOKEN)
ya.upload_file_to_disk('test/netology', 'test.txt')