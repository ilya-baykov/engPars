from task_1 import Connect

"""
     1) Собрать числа с первого столбца и суммировать их.

"""

URL = 'https://parsinger.ru/table/2/index.html'

connect = Connect(URL)
soup = connect.get_soup()

digit_1st_column = []
for tr in soup.find_all("tr"):
    tmp = tr.find('td')
    if tmp:
        digit_1st_column.append(float(tmp.text))
print(sum(digit_1st_column))
