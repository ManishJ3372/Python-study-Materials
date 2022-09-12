# a=10
# print("a= ",a)
# print(id(a))
# print(type(a))
# b=20
# print("b= ",b)
# print(type(b))
# c=40
# print("c= ",c)
# print(type(c))
# a=50
# print(a)
# print(type(a))
# print(id(a))
# print(a)
# b=50
# print(b)
# print(id(b))
#
# #float
# a=10.8
# print(a)
# print(type(a))
# b=2.4
# print(b)
# c=type(b)
# print(c)
# print(type(b))
# d=10.11
# print(d)
# print(id(d))
# e=10.11
# print(e)
# print(id(e))
# a=5.0
# print(a)
# print(id(a))
# b=5.0
# print(b)
# print(id(b))



# i = 0
# while i < 3:
#     print(i)
#     i +=1
# else:
#     print(0)

# A=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# [A[i][len(A)-1-i]for i in range(len(A))]

# print("abcdef".center(7,1))


#1.
# l=[1,9,3,4,7,66]
# for num in l:
#     if num%2==0:
#         print(num)


#2.
# a=1
# b=50
# for num in range(a,b+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#             print(num)

#3.
# def name(fname,lname):
#  print(fname+" "+lname)
# name("Manish","Jakhmola")

#4.
# s=input("Enter string : ")
# print(s[::-1])

#6.
n=int(input("Enter the number : "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#7.
