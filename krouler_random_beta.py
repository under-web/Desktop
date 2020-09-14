import requests
import random

n = 100
s = 0  # счетчик
while n != s:  # цикл если s не равно n , делай цикл
    item = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g', 'j', 'i', 'k',
            'l', 'm', 'n', 'r', 'x', 'w', 'z', 'y', 'u', 'o']  # элементы для генерации случайных адресов
    new_url = random.sample(item, 5)  # создаем случайный список из item обьектов
    new_url = ''.join(new_url)  # приводим список к строковому значению
    url_gen_ru = new_url + '.ru'  # добавляем элемент для получения читаемого адреса url
    # url_gen_com = new_url + '.com' сделать генерацию с доменом .com и др.
    s += 1  # счетчик прибавляем 1

    try:  # пробуем подключиться к адресу
        r = requests.get(url_gen_ru, timeout=5)  # используем аргумент таймаут во избежании зависаний
        print(r.status_code)  # в случае успехатпечатай код подключения
    except requests.exceptions.MissingSchema:  # в случае неудачи ловим исключения
        print('Invalid URL')
