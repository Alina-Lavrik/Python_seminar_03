# Задано N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 4 6 7 -> 5
# 1 3 -> 2
from os import system
system("cls")

spisok = list(map(int, input("Введите числа через пробел: ").split()))

for i in range(1, len(spisok)):
    if spisok[i] -1 == spisok[i - 1]:
        continue
    else:
        print(spisok[i] - 1)


'''with open(f'newfile.txt', 'r') as f1:
    array = f1.read().split()
    array_int = []
    for i in range(len(array)):
        array_int.append(int(array[i]))
    f1.close()

print(array_int)

def Find_the_missing_element (a):
    for i in range(1, len(a)):
        if a[i] - 1 != a[i-1]:
            return a[i] - 1

print(f'Недостающее число последовательности {array_int} - {Find_the_missing_element(array_int)}')'''

