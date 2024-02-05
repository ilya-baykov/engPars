from task_1 import Connect, URL, links_page

"""
    1) Необходимо просмотреть все карточки товаров
        в каждом товаре взять артикул
        сложить все собранные значения
"""

# Получаю ссылки на все мышки на сайте ( на разных страницах )
mouses_links = []
for link in links_page:
    [mouses_links.append(mouse.find('a', class_='name_item')['href']) for mouse in
     Connect(link).get_soup().find_all('div', class_='img_box')]

# Суммирую артиклы всех мышек на сайте
summa_articles = 0
for mouse in mouses_links:
    summa_articles += [int(p.split(': ')[1]) for p in
                       Connect(f"https://parsinger.ru/html/{mouse}").get_soup().find('div', class_='description').find(
                           'p',
                           'article')][
        0]
print(summa_articles)
