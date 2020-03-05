import os


oper = os.name
if oper == 'nt':
	print('У вас windows, поздравляю..')
else:
	pass

l = os.listdir('D:/')
for i in l:
	print(i)

os.makedirs('D:/test', exist_ok = True)
if (os.path.exists('D:/videoplayback.mp4')): # можно сделать рандомизатор файлов видео например
	os.startfile('D:/videoplayback.mp4')
	
