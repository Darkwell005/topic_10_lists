towns: list[str] = input("Введите названия городов через пробел: ").split()
town_list = []
max_len = 0
for town in towns:
    length = len(town)
    if length >= max_len:
        max_len = length
    elif len(town) < max_len:
        pass
print(town_list)
