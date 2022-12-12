'''Реализуйте функцию print_reversed_word_by_symbol(), которая печатает переданное слово посимвольно, как в примере из теории, но делает это в обратном порядке.

word = 'Hexlet'

print_reversed_word_by_symbol(word)
# => 't'
# => 'e'
# => 'l'
# => 'x'
# => 'e'
# => 'H' '''

def print_reversed_word_by_symbol(word):
    for i in list(word)[::-1]:
        print(i)