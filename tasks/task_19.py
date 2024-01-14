hint: str = "Введите числа, разделенные пробелами: "
nums: list[int, ...] = [int(n) for n in input(hint).split()]
length: int = len(nums)
new_list: list[int, ...] = []
for i in range(length):
    for j in range(length):
        if ((nums[i] == nums[j] and i != j) and
                nums[i] not in new_list):
            new_list.append(nums[i])
print(*new_list)
