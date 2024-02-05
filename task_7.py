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

for count, tr in enumerate(soup.find_all("tr")):
    if count == 0:
        print(tr.find_all('th'))
    else:
        current_td = tr.find_all('td')
        print(current_td)
    print()
