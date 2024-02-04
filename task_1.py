import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

"""
    1) Необходимо извлечь название товаров с каждой страницы сайта
        Данные должны хранится в списке
        По итогу работы должен получится вложенный список
"""

URL = 'https://parsinger.ru/html/index3_page_1.html'


class Connect:
    def __init__(self, url, params=None, headers=None):
        self.url = url
        if params:
            self.params = params
        if headers:
            self.headers = headers
        self.headers = {"user-agent": UserAgent().random}
        self.params = {}

    def get_response(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        response.encoding = 'UTF-8'
        return response

    def get_soup(self):
        return BeautifulSoup(self.get_response().text, 'html.parser')


links_page = [f"https://parsinger.ru/html/{link['href']}" for link in
              Connect(URL).get_soup().find('div', class_='pagen').find_all('a')]
mouse_names = {}
for page_link in links_page:
    item = Connect(page_link).get_soup().find_all('div', class_='img_box')
    mouses = [name.find('a', class_='name_item').text for name in item]
    mouse_names.setdefault(page_link, mouses)

with open("mouse_names", "w") as file:
    for link, mouses in mouse_names.items():
        file.write(link + "\n")
        for count, mouse in enumerate(mouses):
            file.write(f'{count + 1})' + "\t" + mouse + "\n")
        file.write('\n\n')
