# 1. Укажите аннотации типов для всех идентификаторов.
example_list = [11, 1, 22, 33, 14, 0, 13, 22, 11, 22, 9, 33]

new_list = []  # Этот список Вам понадобится, но его не нужно выводить
# В условии сказано: Исходный список необходимо модифицировать (изменить).
for x in example_list:
    if x not in new_list:
        new_list.append(x)
print(new_list)  # 2. Нужно вывести example_list без дубликатов

# Подсказка:
# 1. Вам понадобится цикл while, чтобы удалить дубликаты из исходного списка
# 2. Для удаления элемента (дубликата) можете использоввть ключевое слово del
# либо метод pop(индекс_элемента)
