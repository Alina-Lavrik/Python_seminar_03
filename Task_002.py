'''Напишите программу, которая определит _ либо сообщит, что её нет.
Пример:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1 '''

'''from os import system 
system("cls")

stroka = ['kjl', 'lkj', 123, '123','lkj', 'lkj', 'lkm', '123', '123']
# stroka = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
t = 0
p = 0
pos =0

n = input('введите значение ')
while p < 2 and t <len(stroka) - 1:
    if stroka[t] == n:
        p += 1
        pos =t 
    t += 1
if p >1:
    print(pos)
else:
    print(-1) '''

# Вариант 2

mass = ["123", "234", 123, 123, "567", 123]
a = 123

try:
    mass.remove(a)
    print((mass.index(a))+1)
except ValueError:
    print(-1)
