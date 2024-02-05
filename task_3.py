from task_1 import Connect

total_sum = 0
URL = 'https://parsinger.ru/html/index1_page_1.html'

connect = Connect(URL)
soup = connect.get_soup()
nav_menu = {}
for link in soup.find('div', class_='nav_menu').find_all('a'):
    nav_menu[link.text] = link['href']


