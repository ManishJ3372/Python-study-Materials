#polymorphism
#ploy means "many"
#morphy means "form"

#-->polymorphism means "many form"
#eg--> +(add)(concatanation)
#  --->  +multi(repeatition)

#types of polymorphism
#1. method overloading(static early binding,compile time) (not supported in python)
#2. method overriding(dynmic,late binding,run time)

#method overloading -->if 2 method having same name but differnet type of arguments the those method called as method overloading
#eg
#cal(a+b)
#cal(a+b+c+d)
#cal(square)

#but in python method overloading is not supported
#if we are trying to declare multiple method with same name different number of arguments then python will always consider only the last number

#method overriding -->whatever member available in the parent class are by default available to the child class

#method overloading

# class testoverloading:
#     def m1(self):
#         print("no arguments method/function")
#     def m1(self,a):
#         print("one arguments")
#     def m1(self,a,b):
#         print("two arguments")
# obj=testoverloading()
# obj.m1(10,20)

#method overriding

# class A:
#     def p(self):
#         print("hello p")
#     def p1(self):
#         print("hello p1")
# class B(A):
#     def m(self):
#         super().p1()
#         super().p()
#         print("Hiiii m")
#
# obj=8()
# obj.m()
#
# class A:
#     def add(self,a,b):
#         print("add",a+b)
# class B(A):
#     def mul(self,a,b):
#         super().add(10,20)
#         print("multi",a*b)
# obj=8()
# obj.mul(5,4)

## demo program for constructor overriding

# class P:
#     def __init__(self):
#         print("parent")
# class C(P):
#     def __init__(self):
#         print("child")
#         super().__init__()
# obj=C()

