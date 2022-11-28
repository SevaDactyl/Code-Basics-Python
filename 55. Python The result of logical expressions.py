'''Реализуйте функцию string_or_not(), которая проверяет является ли переданный параметр строкой. Если да, то возвращается 'yes' иначе 'no'

string_or_not('Hexlet') # 'yes'
string_or_not(10) # 'no'
string_or_not('') # 'yes'
string_or_not(False) # 'no'
Проверить то, является ли переданный параметр строкой, можно при помощи функции isinstance():

isinstance(3, str) # False
isinstance('Hexlet', str) # True
Поэкспериментируйте с кодом в интерактивном репле https://replit.com/@hexlet/python-basics-logical-expressions'''

def string_or_not(value):
    return isinstance(value, str) and 'yes' or 'no'