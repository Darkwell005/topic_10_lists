mark: list[str] = input("Введите оценки через пробел: ").split()
quantity = len([x for x in mark if int(x) == 2])

if quantity > 1:
    print("Отчислен")
else:
    print("Учится")
