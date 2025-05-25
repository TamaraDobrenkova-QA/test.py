# Conditions
#if
# elif = else if (иначе если)
# else = иначе
# одно условие
user_input = int(input('your number: '))

if user_input == 1:
    print('one')
elif user_input == 2:
    print('two')
elif user_input == 3:
    print('three')
else:
    print('many')
#
# # три отдельных условия
user_input = int(input('your number: '))

if user_input == 1:
    print('one')

if user_input == 2:
    print('two')

if user_input not in [1, 2]:
    print('many')

# проверка валидности ввода пользователя
user_input = input('your number: ')

if user_input.isnumeric():
    user_input = int(user_input)
    if user_input == 1:
        print('one')
    elif user_input == 2:
        print('two')
    elif user_input == 3:
        print('three')
    else:
        print('many')
else:
    print('Enter a number, please')

# Loops - циклы
# for loop - для работы с коллекциями, можно пробежаться по каждому элементу списка
# печататем каждый конкретный элемент коллекции
names = ['John', 'Tom', 'James', 'Bob', 'Jim', 'Bill']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
#
# # печатаем все элементы коллекции
names = ['John', 'Tom', 'James', 'Bob', 'Jim', 'Bill']

for name in names:
    print(name)

#условия для цикла + перенос строки для print
names = ['John', 'Tom', 'James', 'Bob', 'Jim', 'Bill']
for name in names:
    if name.startswith('J'):
        print('Mr.')
    print(name)
#
# # избежать перенос строки при print
names = ['John', 'Tom', 'James', 'Bob', 'Jim', 'Bill']
for name in names:
    if name.startswith('J'):
        print('Mr.', end='')
    print(name)
#
# # для кортежей
names = ('John', 'Tom', 'James', 'Bob', 'Jim', 'Bill')

for name in names:
print(name)

#для словаря
persons = {'John': 132, 'Tom': 167, 'James': 234}
for person in persons:
    print(person)

persons = {'John': 132, 'Tom': 167, 'James': 234}
print(persons.keys())
for person in persons.keys():
    print(person)

persons = {'John': 132, 'Tom': 167, 'James': 234}
print(persons.values())
for person in persons.values():
    print(person)

persons = {'John': 132, 'Tom': 167, 'James': 234}
for person in persons:
    print(f'{person}:{persons[person]}')

persons = {'John': 132, 'Tom': 167, 'James': 234}
print(persons.items())
for person in persons.items():
    name, height = person
    print(f'{name}: {height}')

persons = {'John': 132, 'Tom': 167, 'James': 234}
for name, height in persons.items():
    print(f'{name}: {height}')

#распечатать слова с буквой o и удаляем их из конечного текста
text = 'This is a plain text, for homework'

words = text.split()
fin_words = []
for word in words:
    if 'o' in word:
        print(word)
    else:
        fin_words.append(word)

print(' '.join(fin_words))
