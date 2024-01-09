line: list[str, ...] = input("Введите ваш текст: ").split()
line.sort(key=len, reverse=False)
print(f"Самое длинное слово в предложении: {line[-1]}"
      f"\nСамое короткое слово в предложении: {line[0]}")
# Test: Дом перед персонажем резко обваливается

# Решение рабочее, есть более оптимальный вариант решения:
# Option 2
print(
    f"Самое длинное слово в предложении: {max(line, key=len)}"
    f"\nСамое короткое слово в предложении: {min(line, key=len)}"
)
