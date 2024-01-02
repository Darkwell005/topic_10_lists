num_list = [15, 82, 30, 44, 10]
if not num_list:
    print("Пустой список")
else:
    for x in num_list:
        print(x, num_list.index(x), sep=" ")
