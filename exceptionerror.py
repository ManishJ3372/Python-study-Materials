#what is Exception
#--> an unwanted and unexpected event that disturbs noemal flow of program is called as exception

#eg --
#1.zerodivisionerror
#2.typeerror
#3.value error
#4.filenotfounderror...etc

#exception handaling does not handle exception.

###exception handaling in python
#-->every exception in python is an  object for every exception type the corresponding classes are available

#every exception in python is a class.
#all the exception classes are child classes of baseException. every exception class extends baseExpection
#hence BaseException acts as root of python exception

#customized exception handling by using try-except:-
#its is highly recommended to handle exception
#there are 2 important block i.e try and except

#eg:-
# try:
#     risk code
# except (exception type):
#     handling code or statement
#note:-if try with multiple except block available the default except bolck should be last otherwise we will get syntax error

#finally block:-
#main purpose of finally block is to maintain cleanup code
#try:
#   risky code
#except:
#   handaling code
#finally:
#   cleanup code

# a=int(input("enter number 1 : "))
# b=int(input("enter number 2 : "))
#
# try:
#     print("resource open")
#     print("division",a/b)
#     c=int(input("enter number 3 "))
#
# except ZeroDivisionError as e:
#     print("heyy,you cannot divide a number by zero",e)
# except ValueError as e:
#     print("pls enter number")
# except Exception as e:
#     print("something error")
#
# finally:
#     print("resource close")

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def div(self):
        try:
            c=self.a/self.b
            print(c)
        except Exception as e:
            print("this is the ",e)
try:
    a1=A(10,0)
    a1.div()
except Exception as e:
    print(e)
