import math

# 1.5 0.35 3.06

list1 = input("Введите 3 значения переменных в радианах, разделяя их пробелом (x y z): ").split(" ")

while True:
    if len(list1) != 3:
        list1 = input("Вы должны ввести 3 значения переменных (x y z): ").split(" ")
    else:
        x, y, z = list1
        break

while True:
    try:
        x = float(x)
        break
    except ValueError:
        print("x - не число. Пожалуйста введите число")
        x = input()

while True:
    try:
        y = float(y)
        break
    except ValueError:
        print("y - не число. Пожалуйста введите число")
        y = input()

while True:
    try:
        z = float(z)
        break
    except ValueError:
        print("z - не число. Пожалуйста введите число")
        z = input()

firstAction = 2 * math.asin(math.sqrt(y ** 3 * z * (math.pi * 2)))
secondAction = 7 * x - (math.log(3, 8) * math.asin(math.sqrt(z * y ** 3)))
finalAction = firstAction / secondAction
print(firstAction)
print(secondAction)
print(finalAction)
