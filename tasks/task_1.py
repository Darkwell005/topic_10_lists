# 1. Укажите аннотации типов для всех идентификаторов.
num_list = [15, 82, 30, 44, 10]

if not num_list:
    print("Пустой список")
else:
    # 2. Можно пойти двумя способами: либо через range либо через enumerate
    for x in num_list:
        print(x, num_list.index(x), sep=" ")
