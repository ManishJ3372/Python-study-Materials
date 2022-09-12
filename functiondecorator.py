#Function Decorators:
#Decorator is a function which can take a function as argument and extend its functionality
#and returns modifirf function with extended functionality.

# Input Function
# |
# wish()
# |
# Decorator
# |
# new(add some functionality)
# inner()
#
# the main objective of decorator function is we can extend the functionality of existing
# functions without modifiers that function.

def wish(name):
    print("hello",name,"good morning")

wish("quastech")
wish("durga")

# This function can always print same output for any name
# Hello Durga Good morning
# Hello Ravi Good morning
# hello sunny good morning

# but we want to modify this function to provide different message if name is sunny
# we can do this without touching wish() function by using decorator.

def decor(func):
    def inner(name):
        if name=="sunny":
            print("hello sunny bad morning")
        else:
            func(name)
            return inner
        @decor
        def wish(name):
            print("hello",name,"Good morning")

wish("durga")
wish("ravi")
wish("sunny")

#how to call same function with decorator and without decorator:

#decorator chaining
#we can define multiple decorators for the same function and all these decorators will
#form decorator chaining.
#Eg:-
# @decor1
# @decor
# def num():
#for num() fuction we are applying 2 decorators function.first inner decorator will work
#and then outer decorator.

'''Decorator are very powerful and useful tool in python since it allows programmmers to modify the behaviour
of function or class.decorators allow us to wrap another function in order to extend the behaviour of the wraped function
without permanent modifying it.but before dividing deep into decorators let us understand some concepts that will come in handy
in learning the decorators.

properities of first class functions:

a function is an instance of the object type.
you can store the function in a variable.
you can pass the function as a paramater to another function.
you can return the function from a function. 
'''
#eg 1: Treating the function as objects.
def display():
    print("function line 1")
    print("function line 2")
    print("function line 3")

#rename if display
show=display
show()
d=show
d()
display()

#eg 2: Passing the function a agruments

#eg 3 :returing function from another function
def func(a):
    def func(b):
        return a+b
    return AbaB
sum=AbaB(20)
print("sum",sum(20))