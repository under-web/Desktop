import os
# 1) Программа должна принимать от нас значения 
# 2) Обрабатывать добавляя в начало каждого слова символ #
# 3) В конце должна возвращать все значения уже с символом



def write_data(data):
	with open('data_hash.txt', 'a', encoding='utf8') as f:
		f.write(data)



def main():
	data = input('Введите значения ')
	data = data.split()
	for i in data:
		i = '#' + str(i) + '\n'
		write_data(i)
		print(i) 
	os.system("C:\\Users\\lammer\\Desktop\\data_hash.txt")







if __name__ == '__main__':
	main()
