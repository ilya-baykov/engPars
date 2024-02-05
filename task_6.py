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
print(round(bold_sum, 3))
