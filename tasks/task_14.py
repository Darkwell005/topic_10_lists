# 1. Укажите аннотации типов для всех идентификаторов.
line = input('Введите любую строку: ')
search_word = input('Введите слово для поиска: ')

if search_word not in line:
    print(f'Слово "{search_word}" не существует в строке "{line}"')
else:
    # 2. Лучше использовать enumerate или range,
    # чтобы избавиться от ненужной переменной count
    count = 1
    for x in line.split():
        if x != search_word:
            count += 1
    print(f'Слово "{search_word}" существует в '
          f'строке "{line}" на позиции {count}')
