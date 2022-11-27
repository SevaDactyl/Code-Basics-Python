'''Реализуйте функцию is_palindrome(), которая определяет, является ли слово палиндромом или нет. Палиндром - это слово, которое читается одинаково в обоих направлениях. Слова в функцию могут быть переданы в любом регистре, поэтому сначала нужно привести слово к нижнему регистру: word.lower().

is_palindrome('шалаш') # true
is_palindrome('хекслет') # false
is_palindrome('Довод') # true
is_palindrome('Функция') # false
Реализуйте функцию is_not_palindrome(), которая проверяет что слово НЕ является палиндромом:

is_not_palindrome('шалаш') # false
is_not_palindrome('Ага') # false
is_not_palindrome('хекслет') # true
Для этого, вызовите функцию is_palindrome() внутри is_not_palindrome() и примените отрицание.'''

def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]


def is_not_palindrome(word):
    return not is_palindrome(word)