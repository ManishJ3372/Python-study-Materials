a=10
b=20
c=a+b
print(c)
d=a-b
print(d)

#conditional statements
#if

#syntax ==> if condition:
#               statement...

# name=input("Enter your name : ")
# if name=="quastech":
#     print("this is a condition") #statement
#     print("welcome to quastech!!!") #statement
#
# age=int(input("Enter your age : "))
# if age>=18:
#     print("hello good morning")
#
# age=int(input("Enter your age : "))
# if (age>=18 and age<=100):
#     print("you can give the voting!!!")
#
# name=input("Enter your name : ")
# if (name=="quastech" or name=="Quastech" or name=="QUASTECH"):
#     print("welcome to quastech") #statement
#     print("Hello good evening")  #statement

# if-else conditional statement
#sytnax==> if condition :
#               statements...
#            else
#               statements...

## if condition is true then (if statement) will be executed otherwise (else statements) will be executed

# name=input("Enter the name : ")
# if (name=="python" or name=="django" or name=="java"):
#     print("welcome to quastech...")
# else:                         #false
#     print("Thank you!!!")
#
# age=int(input("Enter your age : "))
# if (age>=18 and age<=75):
#     print("you can give the voting...")
# else:
#     print("sorry !!! you can't give voting...")


#if-elif-else conditional statements
#syntax:===>
#if condition1:
#         statements1
#elif condition2:
#          statemnts2
#elif condition3:
#          statemnts3
#elif condition4:
#          statemnts4
#elif condition5:
#          statemnts5
#   ........
#   ........
#else:
#     statements6...

brand=input("Enter your brand : ")
if brand=="ab":
    print("It is children's brand")
elif brand=="cd":
    print("It is for adults")
elif brand=="fo":
    print("buy one get one free")
else:
    print("other brands are not recommended")


color=input("Enter the color : ")
if color=="red":
    print("It is red")
elif color=="green":
    print("It is green")
elif color=="yellow":
    print("It is yellow")
else:
    print("no match color")

