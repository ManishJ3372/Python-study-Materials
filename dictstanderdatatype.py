#dictionary data type
#-->we can use list,tuple and set to represent a group of individual foa a single entity
#represents with {}
#mutable(we can change)
#value are duplicate

# dict={}
# print(dict)
# print(id(dict))
# print(type(dict))
# print(len(dict))
#
# d={1:"a",2:"a"}
# print(d)
# print(id(d))
# print(type(d))
#
# d[3]="d"
# print(d)
# print(id(d))
# d[4]="e"
# print(type(d))
# print(id(d))
#
# d={1:"a",2:"b",3:"c",4:"d"}
# print(d)
# print(d[1])
# print(d[2])
# print(d[3])
# print(d[4])
# print(d[5])  #error
#
# d={1:"a",2:"b",3:"c",4:"d"}
# print(d.clear())
#
# d={1:"a",2:"b",3:"c",4:"d"}
# d1=d.copy()
# print(d1)
#
# d={1:"a",2:"b",3:"c",4:"d"}
# print(d.keys())
# print(d.values())
# print(d.items())  #key-values pairs as a tuple
#
# d={1:"a",2:"b",3:"c",4:"d"}
# d.pop(1)  #removes specified items
# print(d)
# d.pop(4)  #removes specified items
# print(d)
# d.pop(5)  #keyerror : 5
# print(d)

# d1={1:"a",2:"b",3:"c",4:"d"}
# print(d1)
# print(d1.popitem()) #last items remove
# print(d1)
# print(d1.popitem())
# print(d1)
# print(d1.popitem())
# print(d1)
# print(d1.popitem())
# print(d1)

d={1:"a",2:"b",3:"c",4:"d"}
print(d.setdefault(5,"python"))
print(d)
print(d.setdefault(6,"python"))
print(d)
d1={8:"python"}
d.update(d1)
print(d)
d1.update(d)
print(d1)

d={1:"a",2:"b",3:"c",4:"d"}
d.get(1)
print(d)
print(d.get(1))
print(d.get(5))
print(d.get(4))

d={1:"a",2:"b",3:"c",4:"d"}
print(d.fromkeys("python"))
print(d.fromkeys("2342431"))

print(d.fromkeys("java"))
