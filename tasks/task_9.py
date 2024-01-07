towns: list[str] = input("Введите названия городов через пробел: ").split()

towns.sort(key=len, reverse=True)

print(towns[:3])

# Новосибирск Саратов Волгоград Санкт-Петербург Казань Москва Екатеринбург
