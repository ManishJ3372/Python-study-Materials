#set stander data type
#1.if we want to represent a group of unique values as a single entity then we
#2.duplicate are not allowed
#3.insertion order is not allowed
#4.heterogenous(we can change)
#5.mutable(we can change)
#6.indexing and slicing not allowed for the set
#7.represent with the {}

# s={10,20,30}
# print(s)
# print(type(s))
#
# s={"a","b",100,100,200,False}
# print(s)
# print(id(s))
# print(type(s))
# print(len(s))
#
# s.add(1000)
# print(s)
# print(id(s))
#
# s.add(10)
# print(s)
# print(id(s))
#
#
# s={10,20,30}
# print(s)
# s1=s.copy()
# print(s1)
# s={10,20,30,40,50}
# s.pop()
# print(s)
# s.pop()
# print(s)
#
# s={10,20,30,40,50}
# s.remove(10)
# print(s)
# s.remove(50)
# print(s)
# s.remove(100)
# print(s)
#
# s={10,20,30,40,50}
# s.discard(10)
# print(s)
# s.discard(50)
# print(s)
# s.discard(100)
# print(s)
#
# s={10,20,30,40,50}
# s1=s.clear()
# print(s1)
# print(type(s1))
#
# s={10,20,30}
# s1={40,50}
# s.update(s1)
# print(s)
#
# s1.update(s)
# print(s1)

s={10,20,30}
s1={40,50,60}
print(s.union(s1))
print(s|s1)

print(s.intersection(s1))

print(s.difference(s1))
print(s1.difference(s))