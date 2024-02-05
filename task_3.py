from task_1 import Connect

"""
    1) Необходимо просмотреть все товары
    и найти сумму всех позиций ( количество товаров  * на цену товара )
    
"""

total_sum = 0
URL = 'https://parsinger.ru/html/index1_page_1.html'

connect = Connect(URL)
soup = connect.get_soup()
nav_menu = {link.text: link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')}
pagen_menu = {link.text: link['href'] for link in connect.get_soup().find('div', class_='pagen').find_all('a')}
print(nav_menu)
print(pagen_menu)
