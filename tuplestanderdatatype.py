#tuple stander data type
#sequence of characters
#immutable (we cannot change)
#insertion order is preserved
#duplicates are allowed
#heterogenous object are allowed
#indexing
#we can represent with parenthesis ()

t=()
print(t)
print(id(t))
print(type(t))
print(len(t))

t=("c",10,20,30,20,False)
print(t)
print(id(t))
print(type(t))
print(len(t))

t=(10,30,20,10,40)
print(t)

print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t[0::])
print(t[0:2])
print(t[0:3])

t=(10,70,20,70,50,60,70,100)
print(type(t))
print(min(t))
print(t.count(10))
print(max(t))
print(t.count(10))
print(t.count(70))

t=(20,30,40,50,10)
print(t)
print(type(t))
print((sorted(t)))