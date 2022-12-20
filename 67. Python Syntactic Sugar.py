'''Реализуйте функцию filter_string(), принимающую на вход строку и символ, и возвращающую новую строку, в которой удален переданный символ во всех его позициях.

text = 'If I look back I am lost'
filter_string(text, 'I')  # 'f  look back  am lost'
filter_string(text, 'o')  # 'If I lk back I am lst' '''

def filter_string(text, delete):
    text = text.replace(delete, "")
    return text