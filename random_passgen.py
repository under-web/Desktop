import random

lenSym = int(input('Введите длинну пароля '))

angLang = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y',
           '1', '2', 'Z', '3', '4', '5', '6', '7', '8', '9', '0',
           '!', '@', '#', '$', '%', '^', '&', '*', '_', '+', 'a',
           'b', 'c', 'd', 'f', 'e', 'r', 'm', 'n', 's', 'h', 'g']
result = []
for i in range(lenSym):
    num = random.choices(angLang)
    result += num
result = ''.join(result)
print(result)
