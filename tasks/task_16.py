line: list = input("Введите название городов: ").split()
if "Москва" not in line:
    line.append("Москва")
print(line)
