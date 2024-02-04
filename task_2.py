from task_1 import Connect, URL, links_page

"""
    1) Необходимо просмотреть все карточки товаров
        в каждом товаре взять артикул
        сложить все собранные значения
"""

for link in links_page:
    mouses_links = [mouse.find('a', class_='name_item')['href'] for mouse in
                    Connect(link).get_soup().find_all('div', class_='img_box')]
