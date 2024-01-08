all_fruits: list[str, ...] = ["Гранат", "Ананас", "Слива", "Апельсин", "Виноград",
                              "Киви", "Яблоко", "Манго", "Абрикос", "Грейпфрукт"]
i = 1
fruits: list = []
tropical_fruits: list[str, ...] = [x for x in all_fruits]

for x in all_fruits:
    if i % 2 == 0:
        tropical_fruits.append(x)
    else:
        fruits.append(x)
    i += 1
print(f"Фрукты: {fruits}\nТропические фрукты: {tropical_fruits}")

# Код слишком громоздкий, задачу можно решить в пару строк кода.

# Подсказка: используйте срезы.
