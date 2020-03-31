import requests
from bs4 import BeautifulSoup



def get_html(url):
	r = requests.get(url)
	return r.text

def get_page(html, html0, html1):
	soup = BeautifulSoup(html, 'lxml')
	soup0 = BeautifulSoup(html0, 'lxml')
	soup1 = BeautifulSoup(html1, 'lxml')
	hazard = soup.find('div', class_='total_block col-lg-2 col-sm-4 col-xs-6 offset-md-1').find('span', class_='num').text
	hazard = hazard.split('+')
	try:
		print(hazard[0].center(50), ' Всего зараженных',  '\n')
	except:
		pass
	try:
		print(hazard[1].center(50), 'Прибавилось',  '\n')
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
		
	print('\n', '"Сообщает https://www.gazeta.ru"'.center(80))
	print()
	print()
	print('----------------------------------------------------------')
	# news1_time = soup1.find('ul', class_='news_list news_list_big').find_all('span', class_='news_time')
	news1_txt = soup1.find('ul', class_='news_list news_list_big').find_all('li')
	# for y in news1_time:
		# ty = y.text
	for z in news1_txt:
		yt = z.text
		print(yt.strip())
	print('\n', 'Данные взяты из "https://kazan.mk.ru/news/"'.center(80))
	print()
	print('----------------------------------------------------------')
def main():
	url = 'https://coronavirus-info.ru/'
	url_news = 'https://www.gazeta.ru/subjects/virus.shtml'
	url_news1 = 'https://kazan.mk.ru/news/'
	
	html = get_html(url)
	html0 = get_html(url_news)
	html1 = get_html(url_news1)
	get_page(html, html0, html1)
	








if __name__ == '__main__': # точка входа
	main()
