import requests
from bs4 import BeautifulSoup
 
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'
      }
# -inner su-u-clearfix su-u-trim
url = 'https://mirasskajem.ru/koronavirus-2020-v-rossii/'

r = requests.get(url, headers = headers)

soup = BeautifulSoup(r.text, 'lxml')

ross = soup.find_all('div', class_='su-note')

for i in ross:
	print(i.text, '\n')

input()
