from pprint import pprint

import requests

from yadisk import YandexDisk

TOKEN = ""

if __name__ == '__main__':
    ya = YandexDisk(token="")
    ya.upload_file_to_disk("C:/Users/Саша-Оля/PycharmProjects/netology-requests", "test.txt")