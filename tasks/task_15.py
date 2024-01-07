mark: list[str] = input("Введите оценки через пробел: ").split()
quantity = len([x for x in mark if int(x) == 2])

if quantity > 1:
    print("Отчислен")
else:
    print("Учится")

# Option 2
two_count: int = 0
for x in mark:
    if x == 2:
        two_count += 1
        if two_count > 1:
            print("Отчислен")
            break
else:
    print("Учится")

# 5 4 5 4 3 4 5 2 5 5 5 4
# 5 4 5 4 3 4 5 2 5 2 4 3
