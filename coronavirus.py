import requests
from bs4 import BeautifulSoup

url = 'https://coronavirus-info.ru/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
hazard = soup.find('div', class_='total_block col-lg-2 col-sm-4 col-xs-6 offset-md-1').find('span', class_='num').text
hazard = hazard.split('+')
try:
	print(' Всего зараженных - ', hazard[0], '\n')
except:
	pass
try:
	print('Прибавилось - ', hazard[1])
except:
	pass	
activ = soup.find_all('div', class_='total_block col-lg-2 col-sm-4 col-xs-6')
for i in activ:
	tx = i.text
	print(tx + '\n')
input()


