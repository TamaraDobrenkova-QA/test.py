import math

# устанавливаем значение катетов прямоугольного треугольника
a = 3
b = 4

# находим гипотенузу прямоугольного треугольника
result_a = a * a
result_b = b * b
result = math.sqrt(result_a + result_b)

# выводим результат
print("Гипотенуза прямого треугольника:", result)

# находим площадь прямоугольного треугольника
square = a * b / 2

# выводим результат
print("площадь прямоугольного треугольника:", square)
