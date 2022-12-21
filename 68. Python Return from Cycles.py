'''Реализуйте функцию is_contains_char(), которая проверяет с учётом регистра, содержит ли строка указанную букву. Функция принимает два параметра:

Строка
Буква для поиска
print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => False
print(is_contains_char('Awesomeness', 'm'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False'''

def is_contains_char(string, index):
    return index in string
