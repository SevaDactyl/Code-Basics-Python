'''Найдите символы N и , (запятая) внутри текста в переменной text. Выведите на экран их индексы. Ожидаемый тестами вывод:

Index Of N: 0
Index Of ,: 25
Ваша задача найти эти индексы в строке с помощью метода .find() и вставить в print(), не используя промежуточные переменные. Для разбиения вывода на две строки, вам может понадобится \n'''

text = 'Never forget what you are, for surely the world will not'

# BEGIN
print(f"Index Of N: {text.find('N')}\nIndex Of ,: {text.find(',')}")
# END