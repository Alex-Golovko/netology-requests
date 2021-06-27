from pprint import pprint

import requests

from yadisk import YandexDisk

TOKEN = "AQAAAAAWwSZPAADLW55Sy2uaJEbAlEL1Ms0UfJA"

if __name__ == '__main__':
    ya = YandexDisk(token="AQAAAAAWwSZPAADLW55Sy2uaJEbAlEL1Ms0UfJA")
    ya.upload_file_to_disk("C:/Users/Саша-Оля/PycharmProjects/netology-requests", "test.txt")