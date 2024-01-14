row_count: int = int(input().lstrip('#'))
hash_char: str = '#'

result: list[str, ...] = []
for _ in range(row_count):  # Количество строк кода
    code = input()  # Входная строка кода
    if hash_char in code:  # Проверка
        pos = code.index(hash_char)  # Индекс первого вхождения
        code = code[:pos]  # Удаление комментариев

    code = code.rstrip()  # Очищаем от пробелов
    result.append(code)
print(*result, sep='\n')

"""
#10
result: list[str, ...] = []
for _ in range(row_count):  # Количество строк кода
    code = input()  # Входная строка кода
    if hash_char in code:  # Проверка
        pos = code.index(hash_char)  # Индекс первого вхождения
        code = code[:pos]  # Удаление комментариев

    code = code.strip()  # Очищаем от пробелов
    result.append(code)
print(*result, sep='\n')
"""
