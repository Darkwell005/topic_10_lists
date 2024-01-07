num = int(input("Укажите элемент для удаления: "))
nums: list[int, ...] = [3, 3, 2, 1, 5, 3, 8, 11]

if not nums:
    print("Пустой список")
elif num not in nums:
    print("Не найден")
else:
    result = [x for x in nums if x != num]

    # Option2
    # for x in nums:
    #     if x != num:
    #         result.append(x)

    print(result)
