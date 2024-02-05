from task_1 import Connect

url = 'https://parsinger.ru/table/5/index.html'
connect = Connect(url)
soup = connect.get_soup()

"""
    TASK_001:
    Умножить число в оранжевой ячейке на число в голубой ячейке в той же строке
    и всё суммировать

    * усложнение для себя : если в строке несколько оранжевых ячеек , то необходимо число из каждой такой ячейки 
    умножить на число из голубой ячейки и сложить полученные результаты
"""
total_summa = 0
for count_line, tr in enumerate(soup.find_all('tr')[1:], start=1):
    orange_cells = []
    blue_cells = None
    for count_td, td in enumerate(tr.find_all('td'), start=1):
        if td.get('class') == ['orange']:
            orange_cells.append(float(td.text))
        if count_td == 15:
            blue_cells = float(td.text)
    total_summa += round(sum([digit * blue_cells for digit in orange_cells]), 3)
# print(round(total_summa, 3))

"""
    TASK_002:
    Сформировать словарь,где ключ будет автоматически формироваться из заголовка столбцов,
    а значения это сумма всех чисел в столбце;
    Пример: {'1 column' : 000.000, '2 column' : 000.000, ..., '15 column' : 000.000,}
    
"""
# Формирую список всех элементов
all_elems = []
for count, tr in enumerate(soup.find_all("tr")):
    if count == 0:
        th = tr.find_all('th')
        all_elems.append(th)
    else:
        td = tr.find_all('td')
        all_elems.append(td)

# Прохожу по столбцам среди матрицы всех элементов и создаю результирующий словарь
result_dict = {}
for column in range(len(all_elems[0])):
    result_dict[all_elems[0][column].text] = 0
    for line in range(1, len(all_elems)):
        result_dict[all_elems[0][column].text] += float(all_elems[line][column].text)
    result_dict[all_elems[0][column].text] = round(result_dict[all_elems[0][column].text], 3)

