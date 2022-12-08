'''Реализуйте функцию multiply_numbers_from_range(), которая перемножает числа в указанном диапазоне включая границы диапазона. Пример вызова:

multiply_numbers_from_range(1, 5)  # 1 * 2 * 3 * 4 * 5 = 120
multiply_numbers_from_range(2, 3)  # 2 * 3 = 6
multiply_numbers_from_range(6, 6)  # 6'''

def multiply_numbers_from_range(start, finish):
    result = 1
    for i in range(start, finish + 1):
        result *= i
    return result