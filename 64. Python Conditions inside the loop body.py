'''Функция из теории учитывает регистр букв. То есть A и a с её точки зрения разные символы. Реализуйте вариант этой же функции, так чтобы регистр букв был не важен:

count_chars('HexlEt', 'e')  # 2
count_chars('HexlEt', 'E')  # 2'''

def count_chars(string, char):
    index, count = 0, 0
    string, char = string.lower(), char.lower()
    while index < len(string):
        if string[index] == char:
            # Считаем только подходящие символы
            count = count + 1
        # Счетчик увеличивается в любом случае
        index = index + 1
    return count 