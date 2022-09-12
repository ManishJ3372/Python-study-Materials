#function :- group of statements/block of codes
#python supported 2 types of function
#==a.predefined(built-in functions)
#==b.user defined functions
#function defined using parenthesis

#a.predefined function(id(),type(),input(),eval()...)

#b.user defined function(the function which are developed by programmer)
#syntax==def function name(paramaters)
#           ---------
#           ---------
#           ---------
#return value
#note--> while creating function we can use keyword
#(def)mandatory
#(return)(optional)

# def demo():
#     print("hello GM")
# demo()
# demo()
# demo()

# def wish(name,rollno):
#     print("hello",name,rollno,"good morning")
# wish("quastech",101)
# wish("manish",102)

# def calc(a,b):
#     sum=a + b
#     print(sum)
#     sub=a - b
#     print(sub)
#     div=a / b
#     print(div)
#     mult=a * b
#     print(mult)
# calc(10,20)


#type of arguments/parameters
#1.required argument/positional arguments
#2.keyword argument
#3.variable-length arguments

#1.required argument-->number of arguments should be same in both function call and function defined
#position/order should be followed
#if we change the order then result may be changed
#if we change the number of arguments then we will get error

# def sub(a,b):
#     print("this is a",a)
#     print("this is b",b)
#     print(a-b)
# sub(20,10)
#
# def display(a,b):
#     print(a,b)
# a=20
# b=200
# display(b,a)
# display(b=10,a=20)
# display(20,10)
# display(200,10)

#keyword arguments -->order is not required
#initilization will be done based on keyword(none)
#here the order of arguments is not important but number of arguments must be matched

# def disp(a,b,c):
#     print(a,b,c)
# disp(c=10,a=20,b=25)

#variable-legth arguments-->sometimes we can pass variable number of arguments---
#---to our function such type of arguments are called variable length arguments
#we can declare variable legth argument with
#symbol as follows eg.def fl(*n)
#we can call this function by passing any number of arguments including zero number internally
#---all thesr values represented in the from of type

# def sum(*n):
#     for i in n:
#         print(i)
# sum()
# sum("a")
# sum("a","b")
# sum("a","b","c")
# sum("a","b","c","d")

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mult(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# num1=float(input("Enter first number : "))
# num2=float(input("Enter second number : "))
#
# print("+,-,*,/")
# select=input("select operators : ")
#
# if select =="+":
#     print(num1,"+",num2,"=",add(num1,num2))
# elif select =="-":
#     print(num1,"-",num2,"=",sub(num1,num2))
# elif select =="*":
#     print(num1,"*",num2,"=",mult(num1,num2))
# elif select =="/":
#     print(num1,"/",num2,"=",div(num1,num2))
#
# def sum(*num):
#     t=0
#     for i in num:
#         t=t+i
#         print(t)
# sum()
# sum(10,20)
# sum(10,20,30,40)

# note :- function vs module vs library
#
# function - a group of line with some name is called a function
#
# Function
#
# -------
# ------
# -------
# --------
# -------
# --------
#
# modules-- a group of function saved to a file is called modules
#
# 		MODULES
#
# 	function1	function1
# 	function2	function2
# 	function3	function3
# 	function4	function4
#
# Library-- a group of modules
#
# 		LIBRARY
# 	modules1	modules2
# 	function1	function1
# 	function2	function2
# 	function3	function3
# 	function4	function4

#syntax-->lambda n;n*n

#Anonymous function--nameless function
#eg: Nornal function
#we can define using def keyword

# def sqr(n):
#     return n*n
# print(sqr(5))

#lambda function
#syntax--->lambda n:n*n
# s=lambda n:n*n   #before colon that is input and after colon condition
# print(s(5))

#wap to fing out sum of number
# def sum1(a,b):
#     sum=a+b
#     print(sum)
# sum1(10,20)

a=10
b=20
c=a+b

#lambda version
s=lambda a,b:a+b
print(s(30,20))

#wap to find biggest of given values
def big_num(a,b):
    if(a>b):
        print("a is greater",a)
    else:
        print("b is greater",b)
big_num(40,20)

#lambda version:
s=lambda a,b: a if a>b else b
print(s(40,20))

#with lambda
s=lambda x: True if x%2==0 else False
print(s(10))

#Filter function()
#without lambda
def iseven(x):
    if x%2==0:
        return True
    else:
        return False
print(iseven(10))
def isodd(x):
    if x%2!=0:
        return True
    else:
        return False
print(iseven(10))

#fliter() without lambda
ls=[2,4,5,6,7,8,33,44,77,66,23,11,24,22,90,87,434]
ls1=list(filter(iseven,ls))
ls2=list(filter(isodd,ls))
print(ls1)
print(ls2)

s=lambda x: True if x%2!=0 else False
print(s(10))

#filter with lambda
ls=[2,4,5,6,8,44,33,66,55,22,11,45,67,89,90,113]
ls1=list(filter(s,ls))
print(ls1)
