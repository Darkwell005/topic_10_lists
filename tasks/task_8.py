line = input("Введите ваш текст: ").split()
min_word = ""
max_len = 0
min_len = 0
max_word = ""
for x in line:
    if len(x) > max_len:
        max_len = len(x)
        max_word = x
    elif len(x) < max_len:
        min_len = len(x)
        min_word = x
print(max_word)
print(min_word)
