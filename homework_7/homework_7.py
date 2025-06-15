# угадай число
a = 16
while True:
    user_input = input('Guess my number: ')
    if user_input == 'exit':
        print('Good bye!')
        break
    elif int(user_input) == a:
        print('Congratulations! You guessed the number!')
    else:
        print('Try again!')

# печать словаря
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for word, count in words.items():
    print(word * count)

# извлечь числа и увеличить их на 10

text_1 = 'результат операции: 42'
text_2 = 'результат операции: 54'
text_3 = 'результат работы программы: 209'
print(text_1)
print(text_2)
print(text_3)
def extract_number(text):
    return int(text.split(":")[1].strip())

num1 = extract_number(text_1)  # 42
num2 = extract_number(text_2)  # 54
num3 = extract_number(text_3)  # 209

print(num1, num2, num3)

main_number = 10

def calc(numb):
    print(numb + main_number)

calc(num1)
calc(num2)
calc(num3)

