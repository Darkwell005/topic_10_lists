nums: list[str] = input("Введите числа, разделенные пробелами: ").split()
# Test: 5 4 2 9 3 1 6 8 0
for i in range(1, len(nums)):
    if int(nums[i]) > int(nums[i - 1]):
        print(nums[i], end=" ")
