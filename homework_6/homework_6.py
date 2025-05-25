# добавление ing в конец каждого слова, сохранение пунктуации и регистра
import re

text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

def add_ing_preserve_case(text): # Функция для добавления 'ing' к словам
    def replacer(match):
        word = match.group()
        if word[0].isupper(): # Если слово начинается с заглавной, сохраняем первую букву заглавной
            return word + 'ing'
        else:
            return word + 'ing'
    return re.sub(r'\b\w+\b', replacer, text) # Заменяем каждое слово (\w+) на слово + ing, игнорируя знаки препинания

new_text = add_ing_preserve_case(text)
print(new_text)

# "Fuzz" вместо печати числа,
# а для чисел кратных 5 печатать "Buzz". Для чисел которые кратны одновременно и 3 и 5
# надо печатать "FuzzBuzz". Иначе печатать число.
numbers = list(range(1, 101))

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print('FuzzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print ('Fuzz')
    else:
        print(number)
