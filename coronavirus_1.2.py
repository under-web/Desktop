import requests
from bs4 import BeautifulSoup



def get_html(url):
	r = requests.get(url)
	return r.text

def get_page(html, html0):
	soup = BeautifulSoup(html, 'lxml')
	soup0 = BeautifulSoup(html0, 'lxml')
	hazard = soup.find('div', class_='total_block col-lg-2 col-sm-4 col-xs-6 offset-md-1').find('span', class_='num').text
	hazard = hazard.split('+')
	try:
		print(hazard[0], ' Всего зараженных',  '\n')
	except:
		pass
	try:
		print(hazard[1], 'Прибавилось',  '\n')
	except:
		pass	
	activ = soup.find_all('div', class_='total_block col-lg-2 col-sm-4 col-xs-6')
	for i in activ:
		tx = i.text
		print(tx + '\n')
	news = soup0.find_all('li', class_= 'sausage-list-item')
	for x in news:
		tt = x.text
		print(tt.strip())
	print('\n', '"Сообщает https://www.gazeta.ru"')
def main():
	url = 'https://coronavirus-info.ru/'
	url_news = 'https://www.gazeta.ru/subjects/virus.shtml'
	
	
	html = get_html(url)
	html0 = get_html(url_news)
	get_page(html, html0)
	








if __name__ == '__main__': # точка входа
	main()
