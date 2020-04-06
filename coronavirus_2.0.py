import requests
from bs4 import BeautifulSoup



def get_html(url):
	headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'
      }
	r = requests.get(url, headers = headers)
	return r.text

def get_page(html):
	soup = BeautifulSoup(html, 'lxml')
	print()
	try:
		yand = soup.find('div', class_='covid-speed__description-last covid-speed__line').get_text()
		print('В России  прибавилось - ', yand[2:], '"Yandex.ru"')
	except:
		pass
	print()
	
	try:
		worl = soup.find('div', class_='total_block col-lg-2 col-sm-4 col-xs-6 offset-md-1').find('span', class_='num').text
		worl = worl.split('+')
		print(worl[0].center(50), ' Человек заражено в мире',  '\n')
	except:
		pass
	
	try:
		gazt = soup.find_all('li', class_= 'sausage-list-item')
		
		for x in gazt:
			tt = x.text
			print(tt.strip())
	
	except:
		pass
	
	print()
	
	try:
		kazn = soup.find('ul', class_='news_list news_list_big').find_all('li')
		h = 0
		for z in kazn:
			if h <= 35:
				yt = z.text
				print(yt.strip())
				h += 1
			else:
				break
		print('\n', 'Данные взяты из "https://kazan.mk.ru/news/"'.center(80))
	except:
		pass
	print()
	try:
		ross = soup.find('div', class_='col-xs-12 col-md-8').find_all('ul')
		for i in ross:
			print(i.text, '\n')
	except:
		pass



def main():
	
	url_list = ['https://yandex.ru/', 
	'https://coronavirus-info.ru/', 
	'https://www.gazeta.ru/subjects/virus.shtml', 
	'https://kazan.mk.ru/news/', 
	'https://mirasskajem.ru/koronavirus-2020-v-rossii/' ]
	for i in url_list:
		url = i
		html = get_html(url)
		get_page(html)











if __name__ == '__main__':
	main()
