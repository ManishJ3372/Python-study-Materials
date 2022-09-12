#stander list data type
#1.represents with []
#2.heterogenous object are allowed
#3.mutable
#4.insertion order followed
#5.indexing
#6.duplicate object are allowed

# list=[]
# print(list)
# print(type(list))
# print(id(list))
# list=[1,"python",10,20,True,False,"100",110,25]
# print(list)
# l1=[10,20,30,40,20,30]
# print(l1)

#extend() function
#to add all items at one list to another list

# l1=[10,20,30]
# print(l1)
# print(id(l1))
# l2=[40,50,60]
# l1.extend(l2)
# print(l1)
# print(id(l1))
#
# l1=[10.20,30]
# l2=["a","b","c"]
# l2.extend(l1)
# print(l2)
#
# l1=[True,"python",False]
# l2=["python",10,False,10,45]
# l2.extend(l2)
# print(l2)

#remove() function
#we cna use this function to remove specified item from the list
# l=[10,20,30,40,50,40,70,80]
# l.remove(40)
# print(l)
#
# l1=[1,2,3,4,5,1,5,23,2,3,6]
# l1.remove(5)
# print(l1)

#pop() function
#it reomve and returns the last elements of the list

# l=[10,20,30,40,50]
# print(l)
# l.pop()
# print(l)
# l.pop()
# print(l)
# l.pop()
# print(l)
# l.pop()
# print(l)

# l=[10,20,30,40,50]
# print(l.pop())
# print(l)
# l.pop(0)
# print(l.pop(0))
# print(l)

# l=[50,60,10,40,20,50]
# l.sort()
# print(l)
# l.reverse()
# print(l)

# a=10
# b=20
# print("before swap a=",a)
# print("before swap b=",b)
# c=b-a
# print(c)
# b=c
# print("after swap b",b)
# a*=c
# print("after swap a=",a)
#
#
#
# a=5
# b=6
# a=a+b
# print("a",a)
# b=a-b
# print("b",b)
# a=a-b
# print("a",a)


# a=20
# b=30
# c=50
# a=a+b
# print("swap a",a)
# c=a-b
# print("swap b",b)
# a=a-c
# print("swap c",c)
# b=b+a

#clear() method
l=[10,20,30,30]
l.clear()
print(l)

#copy() method
l=[10,20,30,40]
l1=l.copy()
print(l)
l1[1]=777
print(l1)

l=[1,2,3,4,5,6,7,70]

print(min(l)) #minimum
print(max(l)) #maximum

#count() function
l=[1,2,3,4,5,6,7,78,1,1,2,5,3,21,1,3,1,3]

print(l.count(1))
print(l.count(3))

l=[10,20]
l2=[30,40]
print(l*2)
print(l2*3)

l3=l[1]+l2[1]
print(l3)
