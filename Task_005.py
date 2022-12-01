# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Пример:
# 4, 5 -> 20
# 4, 6 -> 12
# (a, b) = (a * b) / НОД(a, b).

num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))


def calculate_lcm(x, y):
  
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break 
        greater += 1
    return lcm


print("The L.C.M. of", num1, "and", num2, "is", calculate_lcm(num1, num2))


