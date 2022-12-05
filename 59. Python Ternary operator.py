'''Реализуйте функцию flip_flop(), которая принимает на вход строку и, если эта строка равна 'flip', возвращает строку 'flop'. В противном случае функция должна вернуть 'flip'.

Примеры вызова:

print(flip_flop('flip'))  # => 'flop'
print(flip_flop('flop'))  # => 'flip'
Попробуйте написать два варианта функции: с обычным if-else, и с тернарным оператором.'''

def flip_flop(flip):
    if 'flop' == flip:
        return 'flip'
    else:
        return 'flop'
