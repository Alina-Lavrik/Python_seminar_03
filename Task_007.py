# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

from os import system
system("cls")

spisok = [11, 6, 8, 10, 2] 

spisok1 = []

for i in range(0, len(spisok)-1):
    if spisok[i] < spisok[i+1]:
        spisok1.append(spisok[i])
        spisok1.append(spisok[i+1])
print(spisok)
print(spisok1[0:2])


