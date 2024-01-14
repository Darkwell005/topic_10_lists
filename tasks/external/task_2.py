*_, num_1 = input().split(" = ")
*_, num_2 = input().split(" = ")

num_1 = int(num_1)
num_2 = int(num_2)

print([x ** 2 for x in range(num_1, num_2 + 1)])
