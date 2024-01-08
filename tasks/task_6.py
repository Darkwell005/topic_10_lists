from random import randint

# 1. Укажите аннотации типов для всех идентификаторов.
# example_list = [11, 1, 22, 33, 14, 0, 13, 22, 11, 22, 9, 33]

# Список из 15 случайных чисел в диапазоне от 1 до 10
example_list = [randint(1, 10) for _ in range(15)]
print('Before:', example_list)

new_list = []
i = 0
while i < len(example_list):
    if example_list[i] not in new_list:
        new_list.append(example_list[i])
        i += 1
    # здесь можно было просто использовать блок else
    else:
        del example_list[i]

print('After:', example_list)

# Все хорошо, не забудьте указать аннотации и убрать мои комментарии.
