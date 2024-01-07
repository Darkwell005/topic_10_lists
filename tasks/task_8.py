line = input("Введите ваш текст: ").split()
min_word = ""
max_len = 0
min_len = 0  # здесь ошибка
max_word = ""
for x in line:
    if len(x) > max_len:
        max_len = len(x)
        max_word = x
    elif len(x) < max_len:  # и здесь
        min_len = len(x)
        min_word = x
print(max_word)
print(min_word)

# Test: Дом перед персонажем резко обваливается

# Общее замечание: В коде одно и то же много раз
# повторяется (len(элемент) вынесите это в переменную.
