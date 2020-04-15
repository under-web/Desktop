import os
# 1) Программа должна принимать от нас значения 
# 2) Обрабатывать добавляя в начало каждого слова символ #
# 3) В конце должна возвращать все значения уже с символом



def write_data(data):
	'функция описывает запись'
	with open('data_hash.txt', 'a', encoding='utf8') as f: # создает файл если не создан в режиме добавления передает в переменную f
		f.write(data) # переменной f через функцию write записывем данные data



def main():
	data = input('Введите значения ')
	data = data.split()
	for i in data:
		i = '#' + str(i) + '\n'
		write_data(i)
	
	os.system("C:\\Users\\lammer\\Desktop\\data_hash.txt")







if __name__ == '__main__':
	main()





if __name__ == '__main__':
	main()
