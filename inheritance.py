#Inheritance in python.
#It represents real-world relationship well.
#It provides reusability  of a code.
#we don't have to write the same code again and again.
#parent class,child class

#type of inheritance
#1.single inheritance
#2.multilevel inheritance
#3.hybrid inheritance
#4.multiple inheritance

#single inheritance -->

# class parent:
#     def m1(self):
#         print("parent function")
# class child(parent):
#     def m2(self):
#         print("child function")
# obj1=parent()
# obj1.m1()
# obj=child()
# obj.m1()
# obj.m2()

#multilevel inheritance -->

# class A:
#     def a1(self):
#         print("parent function")
# class Bchild(A):
#     def b1(self):
#         print("child function")
# class Cchild(Bchild):
#     def c1(self):
#         print("sub child function")
# obj=Cchild()
# obj.a1()
# obj.b1()
# obj.c1()

#hierarchical inheritance -->

# class parent:
#     def m1(self):
#         print("parent function")
# class child1(parent):
#     def m2(self):
#         print("child1 function")
# class child2(parent):
#     def m3(self):
#         print("child2 function")
# hello=parent()
# hello.m1()
# obj1=child1()
# obj1.m1()
# obj1.m2()
# obj2=child2()
# obj2.m1()
# obj2.m3()

#multiple inheritance -->

# class parent1:
#     def m1(self):
#         print("parent1 function")
# class parent2:
#     def m2(self):
#         print("parent2 function")
# class parent3:
#     def m3(self):
#         print("parent3 function")
# class child(parent1,parent2,parent3):
#     def m4(self):
#         print("child function")
# obj=child()
# obj.m1()
# obj.m2()
# obj.m3()
# obj.m4()

#hybrid inheritance

# class big_parent:
#     def a1(self):
#         print("big parent")
# class parent1(big_parent):
#     def a2(self):
#         print("parent 1")
# class parent2(big_parent):
#     def a3(self):
#         print("parent 2")
# class child(parent1,parent2):
#     def a4(self):
#         print("child")
# class child1(child):
#     def a5(self):
#         print("child 1")
# obj=child1()
# obj.a1()
# obj.a2()
# obj.a3()
# obj.a4()
# obj.a5()
