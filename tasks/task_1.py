num_list: list[int, ...] = [15, 82, 30, 44, 10]

if not num_list:
    print("Пустой список")
else:
    for i in range(len(num_list)):
        print(num_list[i], i, sep=" ")

# Option 2
if not num_list:
    print("Пустой список")
else:
    for idx, item in enumerate(num_list):
        print(item, idx, sep=" ")
