hint: str = "Введите числа, разделенные пробелами: "
nums: list[int, ...] = [int(n) for n in input().split()]

length: int = len(nums)
for i in range(length):
    for j in range(length):
        if nums[i] == nums[j] and i != j:
            break
    else:
        print(nums[i], end=' ')

"""
90 43 5 -7 11 6 32 -1 90 43 21 6 54 5 -6
"""
