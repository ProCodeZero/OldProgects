# Калькулятор минимального уровня

import math

comands = 'Для сложения нажмите +,\nДля вычитания -,\nДля умножения * или х,' \
'\nДля деления нажмите /,\nДля возведения в степень ** или ^,\nДля извлечения квадратного корня,\nЧтобы узнать процент от числа %'
print(comands)

#Ввод данных
n1 = float(input('Введите число '))
fun = input("Введите действие ")

#Всё ещё ввод данных
if fun == '^' or fun == '**':
    n2 = float(input('Введите степень '))
    print(n1 ** n2)

# Квадатный корень
elif fun == '!':
    print(math.sqrt(n1))

#Проценты
elif fun == '%':
    n2 = float(input('Введите количество процентов'))
    rez = n2 * n1 / float(100)
    print(rez)

else:
    n2 = float(input('Введите второе число '))

#Сложение
if fun == '+':
    print(n1 + n2)

#Вычитание
elif fun == '-':
    print(n1 - n2)

#Умножение
elif fun == '*' or fun == "x" or fun == 'х':
    print(n1 * n2)

# Деление
elif fun == '/':
    try:
        print(n1 / n2)
    except ZeroDivisionError:
        print("Делить на ноль нельзя !!!")