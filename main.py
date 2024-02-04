import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

fake_user = UserAgent()
request = requests.get("https://britlex.ru/dictionary.php", headers={"user-agent": fake_user.random})
