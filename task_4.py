import bs4

from task_1 import Connect

"""
     Собрать все уникальные числа из таблицы ( кроме цифр в заголовке )
     и суммировать их

"""

URL = 'https://parsinger.ru/table/1/index.html'
connect = Connect(URL)
soup = connect.get_soup()


def get_unique(soup_: bs4.BeautifulSoup) -> set:
    soup_list = soup_.find_all('td')
    digits = [float(digit.text) for digit in soup_list if soup_list.count(digit) == 1]
    return set(digits)


sum_unique_digits = sum(get_unique(soup))
print(sum_unique_digits)
