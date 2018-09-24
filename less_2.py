#1

import math

a = int(input("enter a "))
b = int(input("enter b "))
c = int(input("enter c "))
D = b**2 - 4 * a * c
print(D)
if D < 0:
    print("The result is a complex value")
elif D == 0:
    x = -b / 2 * a
else:
    x1 = ((-b + math.sqrt(D)) / (2 * a))
    x2 = ((-b - math.sqrt(D)) / (2 * a))
    print(x1, x2)

#2


a = int(input("enter a "))
b = int(input("enter b "))
c = int(input("enter c "))
l_list = [c, b, a]
l_list.sort()

print(f"Medium is: {l_list[1]}")

# Num

# Пользователь вводит два числа, надо вывести на экран в строке, разделённые запятыми, использовать форматирование


a = int(input("enter a "))
b = int(input("enter b "))
x = '{0}, {1}'.format(a, b)

print(x)

# next

