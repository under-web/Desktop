import requests
import random


def url_generator(how):
    score = 0  # создаем счетчик
    while score != how:  # цикл если s не равно n , делай цикл
        item = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g', 'j', 'i', 'k',
                'l', 'm', 'n', 'r', 'x', 'w', 'z', 'y', 'u', 'o', 'rtp',
                'ria', 'gui']  # элементы для генерации случайных адресов

        new_url = random.sample(item, 5)  # создаем случайный список из item обьектов
        new_url = ''.join(new_url)  # приводим список к строковому значению
        url_gen_ru = new_url + '.com'  # добавляем элемент для получения читаемого адреса url
        get_url_cheker(url_gen_ru, score)  # запускаем ф-цию get_url_cheker и передаем ей 2 аргумента (урл и счетчик)
        '''
        Мы сделали 'сплит' значений счетчика 
        передав его в другую локальную переменную x
        '''
        score += 1  # счетчик прибавляем 1


def get_url_cheker(url_gen_ru, x):
    try:  # пробуем подключиться к адресу
        r = requests.get(url_gen_ru, timeout=5)  # используем аргумент таймаут во избежании зависаний
        print(r.status_code, url_gen_ru)  # в случае успеха печатай код подключения и сам адрес

    except requests.exceptions.MissingSchema:  # в случае неудачи ловим исключения
        x += 1  # считаем неудачное подключение
        print('[', x, ']', ' Invalid URL ', url_gen_ru)


def main():
    how = int(input('Print how many iteration: '))  # передали значение количества итераций
    url_generator(how)


if __name__ == '__main__':
    main()

