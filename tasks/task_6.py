# 1. Укажите аннотации типов для всех идентификаторов.
example_list = [11, 1, 22, 33, 14, 0, 13, 22, 11, 22, 9, 33]

new_list = []
i = 0
while i < len(example_list):
    if example_list[i] not in new_list:
        new_list.append(example_list[i])
        i += 1
    elif example_list[i] in new_list:
        del example_list[i]

print(example_list)
