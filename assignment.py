# #1.
# num1=int(input("Enter the first no : "))
# num2=int(input("Enter the second no : "))
# if (num1>= num2):
#     print("num1 is biggest")
# elif (num2 >= num1):
#     print("num2 is biggest")
#
#
#
# #2.
# num1=int(input("Enter the First no : "))
# num2=int(input("Enter the Second no : "))
# num3=int(input("Enter the Third no : "))
# if (num1>= num2 and num1>=num3):
#     print("First is biggest")
# elif (num2>= num1 and num2>=num3):
#     print("Second is biggest")
# else:
#     print("Third is biggest")
#
#
#
#
# #3.
# num1=int(input("Enter the first no : "))
# num2=int(input("Enter the second no : "))
# if (num1<=num2):
#     print("num1 is smallest")
# elif (num2<=num1):
#     print("num2 is smallest")
#
#
#
#
# #4.
# num1=int(input("Enter the First no : "))
# num2=int(input("Enter the Second no : "))
# num3=int(input("Enter the Third no : "))
# if (num1<=num2 and num1<=num3):
#     print("First is smallest")
# elif (num2<=num1 and num2<=num3):
#     print("Second is smallest")
# else:
#     print("Third is smallest")

# import time
# from threading import *
# l=Lock()
# def double(numbers):
#     l.acquire()
#     for n in numbers:
#         time.sleep(1)
#         print("Double : ",2*n)
#     l.release()
# def squre(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Squre : ",n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# t1=Thread(target=double,args=(numbers,))
# t2=Thread(target=double,args=(numbers,))
# t2.start()
# t1.start()
# t1.join()
# t2.join()
# print("The total time taken using thread",time.time()-begintime)

# import time
# from threading import *
#
#
# def job():
#     for i in range(0, 10):
#         print("Child thread")
#         time.sleep(2)
#
#
# t1 = Thread(target=job)
# print(t1.isDaemon())
# t1.setDaemon(True)
# print(t1.isDaemon())
# t1.start()
# t1.join()
# time.sleep(5)
# print("End of main thread")

# f= open("C:/Users/manis/Desktop/py/FileTest.txt",'r')
# print("File Name",f.name)
# print("File Mode",f.mode)
# print("Is file readable",f.readable())
# print("Is file is writeable",f.writeable())
# print(f.read())
# f.close()

# f= open("Python.txt",'w')
# f.write("Java is highlevel programming language\n")
# f.write("Python is highlevel programming language\n")
# f.close()

# f=open("Python.txt",'w')
# list=["sunny\n","test\n","demo\n"]
# f.writelines(list)
# f.write("python java c c++")
# print("List of line written successfully!!")
# f.tell()
# print(f.tell())

# f = open("Python.txt", 'w+')
# list = ["sunny\n", "text\n", "data\n"]
# f.writelines(list)
# f.write("python java c c++")
# print("list of line written successfully!!!")
# a = f.tell()
# print(a)
# print(f.tell())
# print(f.seek(0))
# data = f.readable()
# print(data)
# print(f.read(10))
# f.close()

# f = open("New.txt", 'w+')
# list = ["Quastech\n", "quastech\n", "QUASTECH\n"]
# str = "hello"
# f.writelines(list)
# f.writelines(str)
# f.close()

# f2 = open("python3.jpg", 'w+')
# for j in f2:
#     f2.writelines(f2)

# import pickle
#
# f = open("Text.txt", 'ab')
# list = ["10", 20, 30, "python", True]
# pickle.dump(list, f)
# f.close()
# f = open("Text.txt", 'rb')
# print(pickle.load(f))

# import zipfile
# from zipfile import ZipFile
# import os
#
# f = ZipFile("Modules.zip", "w", 'ZIP_DEFLATED')
# zipf = zipfile.ZipFile("tupleClass", 'w', zipfile.ZIP_DEFLATED)
#
# path = os.getcwd()
# path = path + "/Modules"
#
# zipf.write(path)

import zipfile
from zipfile import *
# file=ZipFile("C:/Users/manis/Desktop/py/file","w",ZIP_DEFLATED)
# file.write("C:/Users/manis/Desktop/py/file.txt")
# file.close()
#
# file1=ZipFile("C:/Users/manis/Desktop/py","r",ZIP_STORED)
# f1=file1.namelist()
# for i in f1:
#     print(1)
# file2=open(i,'r')
# print(file2.read())
# print()

# with ZipFile('spam.zip','w') as myzip:
#     myzip.write('eggs.txt')

# with ZipFile('spam.zip','r') as zipobj:
#     zipobj.extractall('C:/Users/manis/Desktop/py')

# a=[1,2,3,4]
# b=['a','b','c','d']
# print(a)
# print(b)
# c=zip(a,b)
# c=set(c)
# print(c)

# x=36/4*(3+2)*4+2
# print(x)

# import zipfile
# zipfile.ZipFile(r"C:/Users/manis/Desktop/ZIPPING.ZIP",mode='w').write(r"C:/Users/manis/Desktop/zipping.txt")
#
#
# import zipfile
# path_to_zip_file=r"C:/Users/manis/Desktop/ZIPPING.ZIP"
# with zipfile.ZipFile(path_to_zip_file,'r') as zip_ref:
#     zip_ref.extractall(r"C:/Users/manis/Desktop")


import zipfile


# with ZipFile('TEST.zip','w') as myzip:
#     myzip.write('test.txt')

# with ZipFile('TEST.zip','r') as zipobj:
#      zipobj.extractall('C:/Users/manis/Desktop')

#
# a="Hello"
# type(a)

# print("4+6")

# import tkinter
# tkinter._test()
