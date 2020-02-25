import requests
from bs4 import BeautifulSoup
import csv

#https://казань.победа-63.рф/catalog/telefony/1/?q=60&s=new&c=2&cg=142&


def get_html(url):                               #функция с именем 'get_html' принимает аргумент 'url'
	r = requests.get(url)                        # переменная 'r ' включает в себя не структурированный текст из 'url' c помощью метода 'get'
	return r.text 

def get_total_pages(html):
	
	return int(total_pages)










def main():
	url = 'https://казань.победа-63.рф/catalog/telefony/1/?q=20&s=new&c=2&cg=142&'
	base_url = 'https://казань.победа-63.рф/catalog/telefony/'
	page_part = '/?q=20&s=new&c=2&cg=142&'
	
	total_pages = get_total_pages(get_html(url))  #1) получаем общее количество страниц парсинга 
	
	for i in range(1, total_pages):               #2) запускаем цикл 
		url_gen = base_url + str(i) + page_part
		html = get_html(url_gen)
		get_page_data(html)
		
		
