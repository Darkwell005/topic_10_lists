num: int = int(input("Введите целое положительное число: "))

# 1. Укажите аннотации типов для всех идентификаторов.
num_list = [3, 4, 5, 6]
alpha_list = ["a", "b", "c"]

num_list = [num * i for i in num_list]
alpha_list = [num * x for x in alpha_list]

print(num_list)
print(alpha_list)
