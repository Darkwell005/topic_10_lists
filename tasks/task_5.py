num: int = int(input())
example_list: list[int, ...] = [10, -2, 0, 4, -4, 3, 13, -2, 6, -1, 7]

print(len([x for x in example_list if x > num]))

# Option 2
print(sum(1 for x in example_list if x > num))
