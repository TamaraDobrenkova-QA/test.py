# оставляем исходный текст меняем только его части
def generate_text(text1, text2):
    return f'Text consists of the words:{text1} and {text2}'

print(generate_text('Ivan', 'Ivanov'))

# функции генераторы
def progression(limit=100):
    n = 2
    num = 2
    count = 1
    while count < limit:
        yield num
        num += n
        count += 1

count = 1
for number in progression(100000000000000000000000000000000000000000):
    if count == 1000000:
        print(number)
        break
    count += 1

# встроенные модули python
import random

# print()
# input()
# int()

print(f'Your price is {random.random() * 100}')
print(random.randint(0, 5)) # включает оба конца
print(random.randrange(0, 5)) # включает первое не включает последнее число
print(random.randrange(0, 10, 2)) # принт чисел через один

users = ['user1', 'user2', 'user3']
print(random.choice(users))

import sys
print(sys.platform)

# сторонние модули python
# для начала устанавливается на конкретное виртуальное окружение в терминале при помощи команды pip install ...

# создание и импорт собственных модулей - легко при импорте из файла находящегося с той же папке
import helper
helper.helper()
print(helper.variable)

# создание и импорт собственных модулей если файл находится в другой папке - пишем путь от корня
# from test.homework_7_2.assist.py import assist

# если нужна только одна функция из модуля
# from test.homework_7_2.assist.py import var

# если нужна только одна функция из модуля + пернименования
# from test.homework_7_2.assist.py import var as vari
