# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

'''spisok = ['123', 234 , 'sos', '!!!', '__']
n = 0
for i in spisok:

    if type(i) == int or type(i) == float:
        n += 1
if n > 0:
    print('Yes') 
else:
    print('No')'''


# Вариант 2

mass = ['ssss', 'sngujn556', '44', 258]
types = [str(type(i)) for i in mass]
if "<class 'int'>" in types or "<class 'float'>" in types:
    print('Yes')
else:
    print('No')



