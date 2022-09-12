#types of variable--->python support 2 types of variable
#1.GLOBAL VARIABLE
#2.LOCAL VARIABLE

#A.global variable-->the varibale which are declared outside of function
#are called global varibale
#-->the variable can be accesssed in the funtion of that modules

# a=10
#
# def f1():
#     print(a)
# f1()
#
# def f2():
#     print(a)
# f2()
#
# def f3():
#     print(a)
# f3()
#
# def f4():
#     print(a)
# f4()
#
# def f5():
#     print(a)
# f5()

#Local variable-->the variable which are declared inside a function
#are called local variable.
#-->local variable are availabe only for the function in which we declared it i.e from outside of function we cannot access

def f1():
    a=10
    print(a)
    print(a)
    print("f1",a)
f1()

def f2():
    a=20
    print("f2",a)
f2()

b=20
def num1():
    a=10
    c=a+b
    print(a)
    print(b)
    print(c)
def num2():
    b=50
    print(b)
def num3():
    c=40
    print(b)
    print(c)
num1()
num2()
num3()

#global keywords-->we can globally keyword for the following 2 purposes
#1-->To declare global varibale inside function
#2-->to make global variable to the function so that we can perform required modification

def f1():
    global name
    name="python"
    print(name)
f1()
def f2():
    print(name)
f2()

def f3():
    print(name)
f3()

a=10
def f1():
    b=30
    print(a)
    print(b)

