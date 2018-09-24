#1-1.2

name = input("Input your full name?")
age = input("age?")
ques = input("Are u a man?")
ans = ('woman', 'man')[ques == "yes" ]

print("You are " + name + ", Вам " + f"{int(age)} " + "лет, " + ans + " " + ques)


#2.1

a = input("Введите 1 число ")
b = input("Введите 2 число ")

a, b = b, a
print(a, b)

#2

a = input("Введите 1 число ")
b = input("Введите 2 число ")

a = a + b
b = a - b
a = a - b

print(a, b)

