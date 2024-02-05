from task_1 import Connect

"""
    Собрать числа, которые выделены жирным шрифтом
    и суммировать их
"""
bold_sum = 0
url = 'https://parsinger.ru/table/3/index.html'
connect = Connect(url)
soup = connect.get_soup()
raw_bold_digit = [bold.find_all('b') for bold in soup.find_all('tr')]
for line in raw_bold_digit:
    for elem in line:
        bold_sum += float(elem.text)

"""
    Собрать числа, которые выделены в зеленой ячейке 
    и суммировать их
"""

url_2 = 'https://parsinger.ru/table/4/index.html'

connect2 = Connect(url_2)
soup_2 = connect2.get_soup()
green_cell_sum = sum([float(cell.text) for cell in soup_2.find_all('td', class_='green')])
