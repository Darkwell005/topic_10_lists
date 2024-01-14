hint: str = "Введите числа, разделенные пробелами: "
nums: list[int, ...] = [int(n) for n in input(hint).split()]

length: int = len(nums)
for i in range(length):
    left_neighbor: int = nums[i - 1]
    right_neighbor: int = nums[(i + 1) % length]
    print(left_neighbor + right_neighbor, end=' ')

# Option 2
print()
print(
    *[
        nums[i - 1] + nums[(i + 1) % length]
        for i in range(length)
    ]
)

# 4 2 7 5 8 3 13
