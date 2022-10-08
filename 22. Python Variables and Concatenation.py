'''Сайты постоянно посылают письма своим пользователям. Типичная задача — сделать автоматическую отправку персонального письма, где в заголовке будет имя пользователя. Если где-то в базе сайта хранится имя человека в виде строки, то задача генерации заголовка сводится к конкатенации: например, нужно склеить строку Здравствуйте со строкой, где записано имя.

Напишите программу, которая будет генерировать заголовок и тело письма, используя уже готовые переменные, и выводить получившиеся строки на экран.

Для заголовка используйте переменные first_name и greeting, запятую и восклицательный знак. Выведите это на экран в правильном порядке.

Для тела письма используйте переменные info и intro, при этом второе предложение должно быть на новой строке.

Результат на экране будет выглядеть так:

Hello, Joffrey!
Here is important information about your account security.
We couldn't verify your mother's maiden name.
Выполните задание, используя только два print().'''

info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."

first_name = 'Joffrey'
greeting = 'Hello'

# BEGIN
print(greeting + ", " + first_name + "!")
print(intro + "\n" + info)
# END