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
        return requests.get(self.url, headers=self.headers, params=self.params)

    def get_soup(self):
        return BeautifulSoup(self.get_response().text, 'html.parser')


connect = Connect(URL)
soup = connect.get_soup()
links_page = [f"https://parsinger.ru/html/{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
print(links_page)
