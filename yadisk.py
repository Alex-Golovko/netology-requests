import requests
from ya_disk import YandexDisk

TOKEN = 'AQAAAAAWwSZPAADLW55Sy2uaJEbAIEL1Ms0UfJA'

class YandexDisk:
    def __init__(self, token):
        self.file_path = file_path

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        ya = YandexDisk(token=TOKEN)
        ya.upload_file_to_disk('Python', 'test.txt')
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('/home/alexgolovko/PycharmProjects/netology-requests/test.txt')
    result = uploader.upload()

