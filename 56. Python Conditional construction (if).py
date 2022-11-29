'''Реализуйте функцию guess_number(), которая принимает число и проверяет, равно ли число заданному (пусть это будет 42). Если равно, то функция должна вернуть строку 'You win!', в противном случае нужно вернуть строку 'Try again!'.

guess_number(42) # You win!
guess_number(61) # Try again!'''

def guess_number(guess):
    if guess == 42:
        return 'You win!'
    return 'Try again!'