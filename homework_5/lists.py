# распаковка списка и создание переменных
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
a, b, c, d, e = person
print(a, b, c, d, e)

#срез и метод index
list = [42, 514, 9]
a, b, c = list
my_text = f'результат операции: {a}, результат операции: {b}, результат работы программы: {c}'
print(my_text)
a = a + 10
b = b + 10
c = c + 10
my_text_2 = f'результат операции: {a}, результат операции: {b}, результат работы программы: {c}'
print(my_text_2)

# распесатка списков с дополнительной информацией
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
a, b, c = students
d, e, f = subjects
my_text_3 = f'Students {a}, {b}, {c} study these sunjects: {d}, {e}, {f}'
print(my_text_3)

