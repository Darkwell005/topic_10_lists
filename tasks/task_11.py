line: str = input("Введите ваш текст: ")

line_2 = (line.split())
line_2 = line_2[::-1]

print(*line_2)
print(line[::-1])