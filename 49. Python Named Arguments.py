'''Реализуйте функцию trim_and_repeat(), которая принимает три параметра: строку, offset — число символов, на которое нужно обрезать строку слева и repetitions — количество раз, сколько ее нужно повторить, и возвращает получившуюся строку.
Число символов для среза по умолчанию равно 0, а повторений — 1.

text = 'python'
print(trim_and_repeat(text, offset=3, repetitions=2)) # => honhon
print(trim_and_repeat(text, repetitions=3)) # => pythonpythonpython
print(trim_and_repeat(text)) # => python'''

def trim_and_repeat(text, offset=0, repetitions=1):
    return f'{text[offset:] * repetitions}'