# import os


# oper = os.name
# if oper == 'nt':
	# print('У вас windows, поздравляю..')
# else:
	# pass

# l = os.listdir('D:/')
# for i in l:
	# print(i)

# os.makedirs('D:/test', exist_ok = True)
# if (os.path.exists('D:/videoplayback.mp4')): # можно сделать рандомизатор файлов видео например
	# os.startfile('D:/videoplayback.mp4')
	
#110 страница циклы
# town = 'Kazan'
# name = 'Klint'
# weapon = 'Gun'

# slov = {'Town':town,
		# 'Name':name,
		# 'Weapon':weapon
		# }

# for card, contents in slov.items():
	# print('Card', card, 'has contents', contents)

# функция zip()

# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['banana', 'orange', 'peach']
# drinks = ['coffee', 'tea', 'cacao']
# desserts = ['tiramisu', 'ise cream', 'pie', 'pudding']
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
	# print(day, ': drink', drink, 'eat', fruit, 'enjoy', dessert)
# #112 страница
# english = 'Monday', 'Tuesday', 'Wednesday'
# french = 'Lundi', 'Mardi', 'Mercredi'
# print(list(zip(english, french)))
# print(dict(zip(english, french)))

# функция range()

# диапазон 0, 1, 2:

# for x in range(0,3):
	# print(x)

# print(list(range(0,3)))
# #Вот так можно создать диапазон от 2 до 0

# for x in range(2, -1, -1): # первое число говорит от скольки начнем
	# print(x)               # второе число показывает что число будет 0 (т.к. -1 не включается)
                           # # последнее число говорит что шаг будет начинаться с конца (т.к. значение отрицательное)

# В следующем фрагменте кода используется шаг 2, чтобы получить все четные числа от 0 до 10

# print(list(range(0, 11, 2)))

# включения списков

# number_list = []
# for number in range(1, 6):
	# number_list.append(number)
# print(number_list)

# Или же преобразовать в список сам результат работы функции range()

# number_list = list(range(1, 6))
# print(number_list)

#[выражениеforэлементinитерабельный объект]
# number_list = [number for number in range(1,6)]
# print(number_list)

# В первой строке вам нужно, чтобы первая переменная number сформировала
# значения для списка: следует разместить результат работы цикла в переменной 
# number_list. Вторая переменная number является частью цикла for. Чтобы показать
# что первая переменная number является выражением, попробуем такой вариант:

# number_list = [number-1 for number in range(1,6)]
# print(number_list)


# [выражение for элемент in итерабельный объект if условие]

# a_list = [number for number in range(1,6) if number % 2 == 1]
# print(a_list)

# number_list = []

# for number in range(0,6):
	# number_list.append(number)
# print(number_list)

# number_list = list(range(1, 6))

jack = {
		'name':'jack',
		'car': 'bmw'
}

john = {
		'name':'john',
		'car': 'audi'
}

users = [jack, john]

# cars = [person['car'] for person in users]
# print(cars)





