length: int = int(input())  # L — необходимая длина заголовка
n: int = int(input())  # N — количество строк в заголовке новости

title: str = ""
for i in range(n):  # N строк записано по одной строке заголовка.
    title += input()
    if i != n - 1:
        title += "\n"

title_length = len(title)

# title_length -= n - 1  # вычитываем кол-во \n из общей длины
# print('Количество переходов \\n:', title.count('\n'))
slash_n_count = title.count('\n')
dots: str = "..."
if (title_length - slash_n_count) > length:

    slash_n_count = title[:length - 3].count('\n')  # Важно!

    title = title[:length - 3 + slash_n_count] + dots
    print(title)
else:
    print(title)

"""
10
7
123





1234567890
"""

"""
5
2
Первая строка заголовка
продолжение заголовка
"""

"""
3
1
Пер
"""