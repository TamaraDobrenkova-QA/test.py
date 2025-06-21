# вывод зарпалаты и рандобных бонусов
import random

salary_list = [10000, 12000, 13500, 14000, 17000]
results = []
for salary in salary_list:
    bonus = random.choice([True, False])

    if bonus:
        bonus_amount = random.randint(100, 150)
        total = salary + bonus_amount
    else:
        total = salary

    results.append((salary, bonus, f"${total}"))

for salary, bonus, total in results:
    print(f"{salary}, {bonus} -> {total}")

# генерация и печать чисел фибоначи

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci_generator()


target_indices = [4, 199, 999, 9999]
results = {}

for i in range(max(target_indices) + 1):
    number = next(gen)
    if i in target_indices:
        results[i + 1] = number

for index in sorted(results):
    print(f"{index}-е число Фибоначчи: {results[index]}")