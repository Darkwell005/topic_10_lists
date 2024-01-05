num: int = int(input("Введите целое положительное число: "))

num_list: list[int] = [3, 4, 5, 6]
alpha_list = ["a", "b", "c"]

num_list: list[int] = [num * i for i in num_list]
alpha_list: list[str] = [num * x for x in alpha_list]

print(num_list)
print(alpha_list)
