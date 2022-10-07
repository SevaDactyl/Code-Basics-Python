'''Напишите программу, которая берет исходное количество евро, записанное в переменную euros_count, переводит евро в доллары и выводит на экран. Затем полученное значение переводит в рубли и выводит на новой строчке.

Пример вывода для 100 евро:'''

euros_count = 100

# BEGIN
dollars_count = euros_count * 1.25
print(dollars_count)
rubles_count = dollars_count * 60
print(rubles_count)
# END