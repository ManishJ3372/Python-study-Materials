#list =>mutable(we can change)
#represent list[]
#hetrogeneous data type

list=[]
print(list)
list=[1]
print(list)
list=[1,2,3,4,5,6]
print(list)
list=[1,2,2,4,"python",True,10,2,4]
print(list)
print(id(list))
list.append(500)
print(list)
print(id(list))
print(len(list))
print(list[0])
print(list[-5])