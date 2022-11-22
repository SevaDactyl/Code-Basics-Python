'''Реализуйте функцию is_international_phone(), которая проверяет формат указанного телефона. Если телефон начинается с +, значит это международный формат.

is_international_phone('89602223423')  # False
is_international_phone('+79602223423') # True'''

def is_international_phone(phone):
    return phone[0] == '+'