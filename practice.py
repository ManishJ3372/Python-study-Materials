# 1.Factorial of number
# num=int(input("Enter the number : "))
# f=1
# for i in range(1,num+1):
#     f=f*i
# print("Factorial of",num,"=",f)

# 2.GCD or HCF
# n1=int(input("Enter the first number : "))
# n2=int(input("Enter the second number : "))
# if n1<n2:
#     smaller = n1
# else:
#     smaller = n2
# for i in range(1,smaller+1):
#     if n1%i==0 and n2%i==0:
#         gcd=i
# print("GCD of",n1,"and",n2,"is : ",gcd)

# 3.leap year
# year=int(input("Enter a year in 4 digits : "))
# if year%4==0:
#     print("leap year")
# else:
#     print("not a leap year")

# 4.even numbers
# start=200
# end=150
# for num in range(200,150,-1):
#     if num%2==0:
#         print(num, end=" ")
# print()
# print()


# class Rectangle():
#     def __init__(self, l, w):
#         self.length=l
#         self.width=w
#     def area(self):
#         return self.length*self.width
# newRectangle=Rectangle(4,5)
# newRectangle1=Rectangle(5,6)
# print(newRectangle.area())
# print(newRectangle1.area())


# class employee():
#     def getinfo(self, salary, noh):
#         self.salary = salary
#         self.noh = noh
#
#     def addsal(self):
#         if self.salary < 5000:
#             self.salary + 1000
#
#     def addwork(self):
#         if self.noh > 6:
#             self.salary += 1500
#
#     def displaysal(self):
#         print("final salary", self.salary)
#
#
# obj = employee()
# obj.getinfo(10000, 9)
# obj.addsal()
# obj.addwork()
# obj.displaysal()

# myint=10
# def myfunction():
#     myint=20
# myfunction()
# print(myint)

# def multiply(a,b):
#     print(a*b)
# multiply(10,20)

'''
a=(5,6)
b=(7,8)
c=a+b
print(c,type(c))

D1 = {"Rahul": 56, "Virat": 99}
print("Virat" in D1)


Prena = [11, 43, 84, 56, 43, 45, 4, 65, 56, 78, 21, 43, 12, 78, 90, 78, 65, 24, 12, 67]
Ranjana = [12, 35, 42, 65, 39, 57, 46, 65, 66, 25, 21, 93, 92, 58, 30, 28, 53, 41, 27, 79]

Ranjana.extend(Prena)
print('List after extend():', Ranjana)


a=10
b=int("10")
print(a==b)
print(a is b)


6*3+4**2//5-8

L = [10, 14, 18, 22, 'Four numbes']
print(L)

weird
n = 3
24
not weird
'''

# first_name = "Tony"
# last_name = " stark"
# age = 51
# full_name = first_name + last_name
# print(full_name)
# print("Tony is a genius")

# name = input("What is your superhero name? ")
# print(name)

# old_age = input("Enter your old age : ")
# new_age = float(old_age) + 2
# print(new_age)

# first = int(input("Enter the first number : "))
# second = int(input("Enter the second number : "))
#
# sum = first + second
# print("The sum is " + str(sum))

# name = "Manish Jakhmola"
# print(name.find('ak'))
#
# print(name.replace("Manish Jakhmola", "Tushar"))
# print(name)
#
# print("T" in name)

# result = (2 + 4) ** 5
# print(result)

# age = int(input("Enter your age : "))
# if age >= 18:
#     print("you are an adult")
#     print("You can vote")
# elif age < 18 and age > 3:
#     print("you are in school")
# else:
#     print("You are a child")

# first = int(input("Enter first number : "))
# second = int(input("Enter the second number : "))
# operator = input("Enter the operator (+,-,/,*,%) : ")
# if operator == "+":
#     print(first + second)
# elif operator == "-":
#     print(first - second)
# elif operator == "/":
#     print(first / second)
# elif operator == "*":
#     print(first * second)
# elif operator == "%":
#     print(first % second)
# else:
#     print("Exit")

# num = range(10)
# print(num)

# i = 5
# while i >= 0:
#     print(i * "*")
#     i = i - 1

# for i in range(5):
#     print(i + 1)

marks = [93, 12, 32, 45, "bio"]


# print(marks[-2])
# print(marks[0:2])
# for score in marks:
#     print(score)
# marks.append(99)
# marks.insert(0, 99)
# print(marks)
# print(len(marks))
# i = 0
# while i < len(marks):
#     print(marks[i])
#     i = i + 1
# marks.clear()
# print(marks)

# def decorator(func):
#     def inner1():
#         print("hello")
#         func()
#         print("after")
#
#     return inner1
#
#
# def func_to_use():
#     print("This is inside")
#
#
# func_to_use = decorator(func_to_use)
# func_to_use()

# class Demo:
#     def __init__(self):
#         print("This is parent class")
# class Demo2:
#     def __init__(self):
#         print("This is a child class")
#         super().__init__()
# d = Demo2()

# class A:
#     def __init__(self,a,b):
#         print("Parent class")
#         self.a=a
#         self.b=b
#     def add(self):
#         print("Add : ",self.a+self.b)
# class B(A):
#     def __init__(self,a,b):
#         print("Child Class")
#         super().__init__(a,b)
#     def sub(self):
#         print("Sub :",self.a-self.b)
# b = B(34,76)
# b.add()
# b.sub()

# class A:
#     def __init__(self):
#         print("Parent class")
# class B:
#     def __init__(self):
#         print("child class")
# class C(A,B):
#     def __init__(self):
#         print("Second child class")
# c = C()

# d = {'l1':[1,2,3],'l2':[4,11,13],'l3':[5,18,29]}

