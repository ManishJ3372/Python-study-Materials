# class calculator:
#     def add(self, num1, num2):
#         print("addition", num1 + num2)
#
#     def sub(self, num1, num2):
#         print("subraction", num1 - num2)
#
#     def mult(self, num1, num2):
#         print("multiplication", num1 * num2)
#
#     def div(self, num1, num2):
#         print("division", num1 / num2)
#
#     def pwr(self, num1, num2):
#         print("power", num1 ** num2)
#
#     def float(self, num1, num2):
#         print("float", num1 // num2)
#
#     def exit(self):
#         print("Exit")
#
# a1 = "THIS IS A CALCULATOR"
# a2 = len(a1)
# a3 = a1.center(a2)
# print(a3)
# n1 = int(input("Enter the first number : "))
# n2 = int(input("Enter the second number : "))
# obj = calculator()
# while True:
#     print(
#         "press 1 for addition \n "
#         "press 2 for subraction \n "
#         "press 3 for multiplication \n "
#         "press 4 for division \n "
#         "press 5 for power \n "
#         "press 6 for float \n"
#         "press 7 to exit \n")
#     choice = int(input("Enter your choice : "))
#     if choice == 1:
#         obj.add(n1, n2)
#     elif choice == 2:
#         obj.sub(n1, n2)
#     elif choice == 3:
#         obj.mult(n1, n2)
#     elif choice == 4:
#         obj.div(n1, n2)
#     elif choice == 5:
#         obj.pwr(n1, n2)
#     elif choice == 6:
#         obj.float(n1, n2)
#         break
#     else:
#         exit(choice == 7)

# Fruit_Name = {1:'Mangoes', 2:'apples', 3:'Banana', 4:'kiwi'}
# print(Fruit_Name)
#
# class human:
#     Name = None
#     Age = None
#     def get_name(self):
#         print("Enter your name")
#         self.name=input()
#     def get_age(self):
#         print("Enter your age")
#         self.age=input()

class student:
    def __init__(self,name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch
    def print_students(self):
        print("name",self.name)
        print("age", self.age)
        print("branch", self.branch)
student1 = student("manish","25","IT")
student1.print_students()

