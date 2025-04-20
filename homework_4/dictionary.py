#создание элементов
my_tuple = (1, 2, 3, 4, 5)
my_list = [1.2, 2.3, 3.4, 4.5, 5.6]
my_dict = {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5'}
my_set = {True, False, None, 'text1', 'text2'}

#создание словаря
ddict = {'tuple': my_tuple, 'list': my_list, 'dict': my_dict, 'set': my_set}

#печать последнего элемента кортежа
print(my_tuple[-1])

#добавление еще одного элемента в конец списка
my_list.append(6)

#удаление второго элемента списка
my_list.pop(1)

#добавление элемента в словарь
my_dict['I am a tuple,'] = '6'

#удаление элемента словаря
my_dict.pop('0')

#добавление элемента в множество
my_set.add('text3')

#удаление элемента из множества
my_set.discard(None)

#печать словаря
print(ddict)

#второй способ
my_dict = {
    tuple: (1, 2, 3, 4, 5),
    list: [1.5, 2.5, 3.5, 4.5, 5.5],
    dict: {1: True, 2: False, 3: None, 4: True, 5: False},
    set: {'text1', 'text2', 'text3', 'text4', 'text5'}
}

print(my_dict[tuple][-1])
my_dict[list].append(6.5)
my_dict[list].pop(1)
my_dict[dict][('i am a tuple',)] = 6
my_dict[dict].pop(5)
my_dict[set].add('text6')
my_dict[set].discard('text1')
print(my_dict)