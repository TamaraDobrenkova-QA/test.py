# повторении циклов пока не выполнится условие - while

i = 0

while i < 5:
    print('hello')
    i += 1

print('The end')

# остановка цикла while
while True:
    user_input = input('Enter something ')
    if user_input == 'exit':
        break #прерывает всеь шаг кода
    elif user_input == 'skip':
        print('skipping...')
        continue #прерывает теолько текущий шаг
    elif len(user_input) > 10:
          print('Your input is too long')
    else:
        print('input is ok')
print('Good bye!')

# дополнительное использование break и continue
text = 'Sed vitae justo malesuada, commodo libero end eu, bibendum mauris.'

words = text.split()
fin_words = []
for word in words:
    if word == 'end':
        break
    elif 'o' in word:
        print(word)
        continue
    fin_words.append(word)

print(' '.join(fin_words))

# functions
#DRY - don't repeat yourself
a = 1
b = 2
c = 3
d = 4
y = 5

main_number = 47

def calc(numb):  #определение функции, называание функции
    print(numb + main_number)

calc(a)
calc(b)
calc(c)
calc(d)
calc(y)

# не печатать при условии
a = 1
b = 2
c = 3
d = 4
y = 0

main_number = 47

def calc(numb):
    if y == 0:
        print(numb)
    else:
        print(num + main_number)

calc(a)
calc(b)
calc(c)
calc(d)


# решение принимает пользователь
a = 1
b = 2
c = 3
d = 4
y = 1

main_number = 47

def calc(numb):
    if y == 0:
        return numb
    else:
        result = numb + main_number
        return result

calc(a)
calc(b)
calc(c)
calc(d)

# calc(numb) - в скобках указываем параметр, которые принимает функция
# calc(a) - с скобках указан аргумент

# много прпметров

def print_words(first, second, third, fourth, fifth):
    print(f'The first word is {first}, the second word is {second}, {third}, {fourth}, {fifth}')

print_words('one', 'two', 'three', 'four', 'five') # позиционный аргумент
print_words(fifth='five', third='three', fourth='four', first='one', second='two') # именнованный аргумент

#возведение в сетепень
def power(number, degree=2):
    return number ** degree

print(power(2))
print(power(2, 3)) #изменить степень

#
def example(e, f, g, ff='one', gg='two'):
    print(e, f, g, ff, gg)

example(gg=444, e=3, ff=5, g=7, f=0)

#неограниченное количество неименованных позиционных аргументов

def sum_all(*args):
    return sum(args)

print(sum_all(1, 4, 6, 5, 7))

#неограниченное количество именованных позиционных аргументов
def price_list(title, price):
    print(f'Product {title} price is {price}')

price_list('iphone', 2500)
price_list('laptop', 1500)

def price_list(**kwargs):
    for title, price in kwargs.items():
        print(f'Product {title} price is {price}')

price_list(iphone=2500, laptop=1500, sumsung=2000, monitor=1000)