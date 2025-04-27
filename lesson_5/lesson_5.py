#распаковка
my_list = [1, 3]
my_tuple = (2, 6, 9)
a = my_list[0]
b = my_list[1]
c = my_tuple[0]
d = my_tuple[1]
e = my_tuple[2]
#более простой вариант - распаковка
a, b = my_list
c, d, e = my_tuple
print(a, b, c, d, e)

#срез - получение части списка
lll = [1, 3, 5, 2, 5, 7, 1, 3]
print(lll)
print(lll[0:4]) #от - включительно, до - не включительно
print(lll[ :4]) #от начала и до какого-то элемента
print(lll[3:]) #от какого-то элемента и до конца
print(lll[1::2]) #установили шаг среза в 2
print(lll[:]) #распечатать все
print(lll[::-1]) # распечатать все, но считать с конца
print(lll[-2:-6:-1])

#методы строк
text = 'my long long string'
print(text[3]) #печать четвернотого по счету элемента
print(len(text)) # общее количество элементов
print(text.index('l')) #найти позицию символа
print(text.index('long')) #найти позицию слова
print('long' in text) # есть ли слово в тексте
print('Long' in text) # есть ли слово в тексте
print(text.count('long')) #посчитать слова
print(text.count('l')) # посчитать символы
print(text.find('long')) #найти слово
print(text.find('lone')) #найти слово
print(text[:7]) #срез
print(text.startswith('my')) #проверка верности утверждения
print(text.startswith('mu')) #проверка верности утверждения
print(text.endswith('string')) #проверка верности утверждения
print(text.endswith('strings')) #проверка верности утверждения

#
text = 'thIs tExT iS wiTH meSsEd uP CapiTalIzaTIon'
print(text.capitalize()) #делает первую букву заглавное
print(text.title()) #делает каждую первую букву заглавными
print(text.upper()) #делает все заглавными
print(text.lower()) #делает все маленькими

#поменять регистр разных слов
txt = 'MY LONG long stRing'
string_index = txt.lower().index('string') #превращает всю строку в нижний регистр и ищет индекс слова string
print(txt[:string_index].lower() + txt[string_index:].upper())

#изменять строку, перезаписывать значений
msg = 'Hello world!'
msg = msg.replace('world', 'universe')
print(msg)

#обрезка пробелов
txt = ' admin '
txt = txt.strip()
print(txt)

text = ' friend '
text = text.rstrip()
text = text.lstrip()
print(text)

texts = '"name"'
texts = texts.strip('"')
print(texts)

#преоблазование строик в список и наоборот
my_string = 'some little text'
my_string2 = 'some,little,text'
list_from_text = my_string.split() # разделяет строку по пробелам
list_from_text2 = my_string2.split(',') # разделяет строку по запятым
print(list_from_text)
print(list_from_text2)

languages = ['Python', 'Java', 'Ruby']
print(languages)
languages = ', '.join(languages) #соединяем элементы запятой и пробелом
print(languages)

#форматирование строки
a = 'one'
b = 'two'
print('Fist word is', a, ', second word is', b) #появляются лишние пробелы

my_text = 'First word is ' + a + ', second word is ' + b #конкотенация
print(my_text)

my_text = 'First word is %s, second word is %s' # подстановка, старый способ
print(my_text % (a, b))

my_text = 'First word is {}, second word is {}' #более современный сопосб нерекоммендуемый формат
print(my_text.format(a, b))

my_text = 'First word is {0}, second word is {1}' #более современный сопосб рекоммендуемый формат
print(my_text.format(a, b))

#f-string - самы наглядный способ
my_text = f'First word is {a}, second word is {b}'
print(my_text)

template = 'Hello, {0}!'
username = input('What is your name?')
print(template.format(username))
