#операторы составного присваивания
a = 1
b = 2
#a = a + 1
a += 1
#b = b - 1
b -+ 1
print(a, b)

#кокнкотенация
print('text' + 'text')

text = 'text'
#text = text + ' new'
text += ' new'
print(text)

print('-' * 20)
print('Copyright')
print('-' * 20)

symbol = '-'
symbol *= 40
print(symbol)
print('Copyright')
print(symbol)

#операторы принадлежности in, not in
text = 'I love Python'
print('love' in text)
print('Love' in text)

#операторы идентичности is, is not
b = 2
c = 2
d = 257
e = 257
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(b is c)
print(d is not e)

#способы ввода данных (клавиатура) - ввод всегда воспринимается как строка
user_name = input('What is your name?')
print('Hello', user_name, '!')

#узнать тип введенных данных
user_input = int(input('Enter something'))
print(type(user_input))
print(2 + user_input)

#преобразование типов данных
a = ('1')
print(type(a))
a = int(a)
print(type(a))
a = str(a)
print(type(a))
b = 'True'
print(type(b))
b = bool(b)
print(type(b))
print(b)
a = float(a)
print(type(a))
print(a)

#типы данных (list - списки)
my_list = [1, 3, 6, 7, None, 'text', False, 2.42, 'sdsdf', 'last', 'last one']
print(my_list)
print(my_list[2])
print(my_list[0])
print(my_list[9])
#печать последнего элемента в списке
print(my_list[-1])

#изменение элемента по индексу
my_list[2] = 42
print(my_list)

#создание пустого списка
my_list = []
my_list_2 = list()

#добавление элемента в список
my_list.append(54)
my_list.append(42)
my_list_2.append('text')
print(my_list)
print(my_list_2)

#считаем количество элементов в списке
print(len(my_list))

#найти позицию элемента в строке
print(my_list.index(42))

#удаление элементов из списка
popped = my_list.pop(0)
print(my_list)
print(popped)

#поиск внутри списка
print(42 in my_list)
print(54 in my_list)

#tupple - картеж - хранить списки, но это не изменяемый тип данных (запятая обязательна, даже если в нем один элемент)
my_tupple = (1, 3, 6, 7, None, 'text', False, 2.42)
print(my_tupple[2])
print(my_tupple[-1])

#создание пустого картежа
my_tuple = ()
my_tuple = tuple()
my_tuple = (1, 5, 2, 6, 1, 8, 9, 13)
print(my_tuple)

#подсчет сколько раз элемент встречается внутри коллекции или картежа
print(my_tuple.count(1))
print(my_tuple.index(5))

#set - множуство - содержет в себе только не повторяющиеся элементы, не гарантирует порядок элементов
my_set = {1, 3, 3, 6, 7, 7,  None, 'text', False, 2.42}
my_set.add(42)
my_set.add('text')
print(my_set)

#перобразование
list1 = [1, 2, 5, 6, 2, 1, 8]
print(list1)
list1 = set(list1)
print(list1)
list1 = list(list1)
print(list1)

#создание пустого set
#Это словарь
my_set = {}
print(type(my_set))
#это пустой set
my_set = set()
print(type(my_set))

#словарь - dictionary
my_dict = {'one': 'value1', 'two': 'value2'}
my_dict_2 = {}
print(my_dict['one'])
print(len(my_dict))
my_dict['one'] = 'myvalue'
print(my_dict)
my_dict['three'] = 'value3'
print(my_dict)
my_dict['four'] = False
my_dict['five'] = [1, 5, 10]
my_dict['six'] = {1, 6, 9}
print(my_dict)
my_dict[2] = 'asd'
my_dict[False] = '68798'
my_dict[2.42] = 'sdfsd'
my_dict[(1, 2)] = 'sdfgsd'
my_dict[5] = {1: 2}
print(my_dict)

#все ключи словаря
print(my_dict.keys())
#все значения словаря
print(my_dict.values())
#все ключи и значения словаря
print(my_dict.items())


