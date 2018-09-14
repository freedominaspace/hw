#1-1.2

name = input("Input your full name?")
age = str(input("How old are you?"))
ques = input("Are u a man?")
ans = ('woman', 'man')[ques == "yes"]
man = "male"
woman = "female"
yes = True
no = False

print("You are " + name + ", Вам " + age + "лет, " + ans + " " + ques)



#2.1

a = input("Введите 1 число ")
b = input("Введите 2 число ")

a, b = b, a
print(a, b)

#2

a = input("Введите 1 число ")
b = input("Введите 2 число ")
print(a, b)

c = [b, a]
print(c)

