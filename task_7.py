from task_1 import Connect

"""
    Умножить число в оранжевой ячейке на число в голубой ячейке в той же строке
    и всё суммировать
    
    * усложнение для себя : если в строке несколько оранжевых ячеек , то необходимо число из каждой такой ячейки 
    умножить на число из голубой ячейки и сложить полученные результаты
"""
url = 'https://parsinger.ru/table/5/index.html'
connect = Connect(url)
soup = connect.get_soup()
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
print(round(total_summa, 3))
