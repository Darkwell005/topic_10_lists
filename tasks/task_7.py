num = int(input("Укажите элемент для удаления: "))
num_list = [3, 3, 2, 1, 5, 3, 8, 11]
if num not in num_list:
    print("Не найден")
else:
    while num in num_list:
        num_list.remove(num)
    print(num_list)
