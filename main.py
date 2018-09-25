1-1.2

name = input("Input your full name?")
age = input("age?")
ques = input("Are u a man?")
ans = ('woman', 'man')[ques == "yes" ]

print("You are " + name + ", Вам " + f"{int(age)} " + "лет, " + ans + " " + ques)


# 2.1

a = input("Введите 1 число ")
b = input("Введите 2 число ")

a, b = b, a
print(a, b)

#2
#var2 Сокращённый вариант(додумал не сам) 

a = int(input("Введите 1 число "))
b = int(input("Введите 2 число "))

a += b
b = (a - b)
a -= b

print(a, b)

# #var1
#
# a = a + b
# b = a - b
# a = a - b

#2.2

a = 3
b = 2

c = a
a = b
b = c

print(a, b)
