# Соблюдайте PEP8
all_fruits: list[str, ...] = [
    "Гранат", "Ананас", "Слива", "Апельсин", "Виноград",
    "Киви", "Яблоко", "Манго", "Абрикос", "Грейпфрукт"
]

fruits: list[str, ...] = all_fruits[0::2]
tropical_fruits: list[str, ...] = all_fruits[1::2]

print(f"Фрукты: {fruits}\nТропические фрукты: {tropical_fruits}")
