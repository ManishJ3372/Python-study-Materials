# oops-->object oriented programming languange
# --aaaa.oops is way of structuring a program into class, object,method(function) or constructor
# In real-world everything is object

# class-->A class is a blueprint or template for a particular object which tells that how particular object will
# behave when passed into blueprint or template known to us class
# self is not default keyword

# we can write a class to repsetn attributes and action of obejct
# properities can be repsresnted by variabke
# action can be represnt by method

# note-->1.In python every thing is an object
# 2.To create object we required same model or plan and action of obejct
# 3.we can write a class to represent properities and actio of objetc

# class define state and behaviours of object
# what object knows its variable with object does it method

# how to define class
# we can define class by using class keyword

# syntax-->class class_name:
# variable: local,globak,instance
# print(class_name.__doc__)
# print(help(class_name)

# documentation string reprensent desc of the class within doc sting is always optional
# a.print(class_name.__doc__)
# b.print(class_name)

# eg:-

class demo:
    '''this is demo class'''


print(demo.__doc__)


# Three types of variable in python
# 1.instance variable
# 2.static variable
# 3.global variable

# class          student

# attributes     r.no.name.count

# oops concepts in python

# class          class
# object
# abstraction
# encaspulation
# Inheritance
# plomorphism

# class
# 1.blueprint which is followed by objects
# 2.logical structure with behaviour

# object
# instance of a class

# self variable:-
# self is a default variable which always pointing to current object(like this keyword in java)

# by uisng self we can access instance variable and isntance methods of object

# Note:-
# 1.self should be first parameter inside constructor
# def __init__(self): #constructor

# 2.self should be first parameter inside class method
# def test(self):

# Constructor-->
# 1.construcntor is a special method in python
# 2.the name of constructor should be __init__(self)
# 3.constructor will execute automatic at the time of object creation
# 4.constructor can take at leas one argument (self)

# eg==>
# def __init__(self,name,r_no,location)
#               self.name
#               self.r_no
#               self.location

# generator
# 1.generator is a function which is resopnsible to generate a sequence of values
# 2.we cam write generator function just like ordinary function , but w=it uses void
# kwyword to return vakues

# generator
# a.selquence of values
# b.yield

def mygenerator():
    yield "a"
    yield "b"
    yield "c"
    yield "10"


mygenerator()
m = mygenerator()
print(m)
print(type)


def wish(name):
    print("good morning", name)


wish("python")
g = wish
g("java")
greeting = wish
greeting("java")
hello = wish
hello = ("django")


def test():
    yield "10"
    yield "20"
    yield "30"


print(type(test))
q = test()
print(type(g))
print(next(g))
print(next(g))
print(next(g))


# wap generate 10 numbers

def firstnum(num):
    n = 1
    while n <= num:
        yield n
        n = n + 1


values = firstnum(10)
for x in values:
    print(x)


def firstnum(num):
    n = 1
    while n <= num:
        yield n
        n = n + 1


values = firstnum(20)
l = list(values)
print(l)
for x in values:
    print(x)
