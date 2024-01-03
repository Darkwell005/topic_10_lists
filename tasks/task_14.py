line = input('Введите любую строку: ')
search_word = input('Введите слово для поиска: ')
if search_word not in line:
    print(f'Слово "{search_word}" '
          f'не существует в строке "{line}"')
else:
    count = 1
    for x in line.split():
        if x != search_word:
            count += 1
    print(f'Слово "{search_word}" '
          f'существует в строке "{line}" '
          f'на позиции {count}')
