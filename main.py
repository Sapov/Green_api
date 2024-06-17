import requests
import os
from dotenv import load_dotenv

load_dotenv()


class WhatsAppMsg:
    idInstance = os.getenv('idInstance')
    apiTokenInstance = os.getenv('apiTokenInstance')
    apiUrl = os.getenv('apiUrl')

    def __init__(self, phone: str, message: str):
        self.message = f'"{message}"'
        self.phone = phone

    def send_message(self):
        URL = f"{self.apiUrl}/waInstance{self.idInstance}/sendMessage/{self.apiTokenInstance}"
        payload = '{\r\n\t"chatId": "' + self.phone + '@c.us",\r\n\t"message":' + self.message + '\r\n}'
        print(f'[PAYLOAD] {payload} ')
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", URL, headers=headers, data=payload)
        print(response.text.encode('utf8'))

    def send_pictures(self, caption: str, pic_link: str):
        url_pic = f"{self.apiUrl}/waInstance{self.idInstance}/sendFileByUrl/{self.apiTokenInstance}"

        payload = ('{\r\n   \t\"chatId\": \"' + self.phone + '@c.us\",\r\n\t\"urlFile\": \"' + pic_link
                   + '\",\r\n\t\"fileName\": \"horse.png\",\r\n\t\"caption\": \"' + caption + '\"\r\n}')
        print(payload)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url_pic, headers=headers, data=payload)

        print(response.text.encode('utf8'))

    def get_contact(self):
        url = f"{self.apiUrl}/waInstance{self.idInstance}/getContacts/{self.apiTokenInstance}"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        # print(response.text.encode('utf-8'))
        print(type(response.json()))
        res = response.json()
        print(res)
        try:
            for i, v in enumerate(res):
                print('#', i, v['id'], '\t', v['name'], '\t', v.get('contactName', 'No Name'))
        except KeyError:
            print("Ключ не найден!")  # Так мы обнаруживаем отсутствие такого ключа в словаре.


if __name__ == '__main__':
    # отправить сообщение
    # WhatsAppMsg(os.getenv('MY_TEL'), "Текст Vjyjuj vМтного много текста в месеенджер").send_message()
    #
    # Отправить картинку
    # pic_link = 'https://order.san-cd.ru/media/image/11_075_440_%D0%B3%D1%80%D0%B0%D0%BC%D0%BC_%D0%BB%D1%8E%D0%B2%D0%B5%D1%80%D1%81%D1%8B_.tif.100x0_q85.jpg'
    #
    # WhatsAppMsg(os.getenv('MY_TEL'), "Текст для отсылки в месеенджер").send_pictures('это название файла (надпись)', pic_link)
    WhatsAppMsg(os.getenv('MY_TEL'), "Текст для отсылки в месеенджер").get_contact()
