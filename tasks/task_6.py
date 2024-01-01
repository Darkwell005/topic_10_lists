example_list = [11, 1, 22, 33, 14, 0, 13, 22, 11, 22, 9, 33]
new_list = []
for x in example_list:
    if x not in new_list:
        new_list.append(x)
print(new_list)
