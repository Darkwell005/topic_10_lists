line = input("Введите ваш текст: ").split()
print(len([word for word in
           line if len(word) > 3]))
