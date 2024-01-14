hint: str = "Введите числа, разделенные пробелами: "
nums: list[int, ...] = [int(n) for n in input(hint).split()]

length: int = len(nums)
new_list: list[int, ...] = []
for i in range(length):
    for j in range(length):
        if nums[i] == nums[j] and i != j:
            new_list.append(nums[i])
            break

print(*new_list)

# 1 9 7 3 6 2 7 3 4 3
