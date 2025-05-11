# распаковка списка и создание переменных
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
a, b, c, d, e = person
print(a, b, c, d, e)

#срез и метод index
text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'
print(text_1)
print(text_2)
print(text_3)

index_1 = text_1.index(":")+1
index_2 = text_2.index(":")+1
index_3 = text_3.index(":")+1
num_1 = int(text_1[text_1.index(":") + 1:]) + 10
num_2 = int(text_2[text_2.index(":") + 1:]) + 10
num_3 = int(text_3[text_3.index(":") + 1:]) + 10
text_1_updated = text_1[:index_1] + str(num_1)
text_2_updated = text_2[:index_2] + str(num_2)
text_3_updated = text_3[:index_3] + str(num_3)

print(text_1_updated)
print(text_2_updated)
print(text_3_updated)

# list = [42, 514, 9]
# a, b, c = list
# my_text = f'результат операции: {a}, результат операции: {b}, результат работы программы: {c}'
# print(my_text)
# a = a + 10
# b = b + 10
# c = c + 10
# my_text_2 = f'результат операции: {a}, результат операции: {b}, результат работы программы: {c}'
# print(my_text_2)

# распечатка списков с дополнительной информацией
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
a, b, c = students
d, e, f = subjects
my_text_3 = f'Students {a}, {b}, {c} study these sunjects: {d}, {e}, {f}'
print(my_text_3)

