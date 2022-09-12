# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

n=int(input("Enter the number : "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

# n=int(input("Enter number of rows : "))
# for i in range(1,n+1):
#     print(" "*(i-1),end="")
#     for j in range(1,n+2-i):
#         print("*",end="")
#     print()

# n=int(input("Enter the numbers : "))
# for i in range(n):
#     print(i)
#     for j in range(1,n+1):
#         print(chr(64+1),end="")
#     print()

# n=int(input("Enter the numbers : "))
# for i in range(1,n+1):
#     for j in range(1,6):
#         print(chr(64+j),end="")
#     print()

# n=int(input("Enter number of rows : "))
# for i in range(1,n+1):
#     print(" "*(i-1),end="")
#     for j in range(1,n+2-i):
#         print(chr(64+i),end="")
#     print()

# n=int(input("Enter the numbers : "))
# sum=0
# temp=n
# while n>0:
#     sum=sum+(n%10)*(n%10)*(n%10)
#     n=n//10
# if n==sum:
#     print(n,"yes")
# else:
#     print(n,"no")

# a=0
# b=1
# z=0
# n=int(input("Enter number : "))
# while z<=n:
#     print(z)
#     a=b
#     b=z
#     z=a+b

# l=[1,2,3]
# #print(l)
# l.append([3,4])
# l.append((2,3,4))
# print(len(l))

# s="quastech"
# print(s[::-1])
# a=reversed(s)

# def rev(s):
#     str=""
#     for i in s:
#         str=i+str
#     return str
# s="python java quastech"
# print(rev(s))
#
# s=input("Enter string : ")
# str=len(s)-1
# t=''
# while str>=0:
#     t=t+s[str]
#     str=str-1
# print(t)