line: str = input("Введите ваш текст: ")

line_2: list[str, ...] = line.split()
print(*line_2[::-1])
print(line[::-1])

# print(*[word[::-1] for word in line_2][::-1])

# Молодой парень, пинающий камни на дороге
