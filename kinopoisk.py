import requests
from bs4 import BeautifulSoup
import csv

# 1. вводим название фильма
# 2. получаем ответ с выводом на экран и записью в csv


def get_html(base_url):
	r = requests.get(base_url)
	return r.text

def get_html_data(html):
	soup = BeautifulSoup(html, 'lxml')
	try:
		title = soup.find('div', class_='search_results').find('span', class_='gray').text
	except:
		title = ''
		print('пусто')
	try:
		prod = soup.find('div', class_='search_results').find('span', class_='year').text
	except:
		prod = ''
		print('пусто')
	
	try:
		reit = soup.find('div', class_='search_results').find('div', class_='rating ratingGreenBG').get('title')
	except:
		reit = ''
		print('0')
	try:
		boss = soup.find('div', class_='search_results').find('i', class_='director').text
	except:
		boss = ''
		print('нет')
	
	print(title + '\n' + prod + '\n' + reit + '\n' + boss)
	
	data = {'title':title,
			'prod':prod,
			'reit':reit
			}
	
	write_csv(data)


def write_csv(data):
	with open('kinopoisk.csv', 'a', encoding='utf8') as wr:
		writer = csv.writer(wr)
		writer.writerow((data['title'],
						data['prod'],
						data['reit']
						))

def main():
	url = 'https://www.kinopoisk.ru/index.php?kp_query='
	quest = input('О каком фильме будем искать информацию?   ')
	gen_url = url + str(quest)
	html = get_html(gen_url)
	get_html_data(html)






















if __name__ == '__main__':
	main()
