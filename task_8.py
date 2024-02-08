import csv
from task_1 import Connect

URL = 'https://parsinger.ru/html/index3_page_1.html'
connect = Connect(URL)
soup = connect.get_soup()

pagen_links = [f"https://parsinger.ru/html/{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]

all_product = []
for link in pagen_links:
    items_on_page = Connect(url=link).get_soup().find_all('div', 'item')
    for item in items_on_page:
        name = item.find('a', class_='name_item').text.strip()
        price = item.find('p', class_='price').text
        brand, type_mouse, connection, is_gamer = [info.text.split(':')[1] for info in
                                                   item.find('div', class_='description').find_all('li')]
