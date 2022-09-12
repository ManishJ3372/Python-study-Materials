#int -->we can int to represent whole numbers(intergral values)
a=5
b=type(a)
print(a)
print(b)
print(type(a))
print(id(a))

#float data types -->we can use float data types to represent floating point
f=1.05
print(type(f))
print(id(f))
print(f)

#complex data types
d=1.4+2.3j
print(d)
print(type(d))
print(id(d))

e=5+25j
print(e)
m=e.real
print(m)
print(type(m))

#bool data type -->we can use this data type to represent boolean values(True or False)
#True=1
#False=0
a=True
print(a)
print(type(a))
a=False
print(a)
print(type(a))

b=True+True
print(b)
print(type(b))        #return(class int)
c=False+False
print(c)
print(type(c))        #return(class int)

#string data type(str)-->A sequence of characters enclosed within single quotes(' ') or double quotes(" ")

a='python'
print(a)
print(type(a))


a='''     A/606,
     Paradise Tower,
     Behind new viva college,
     Virar(w) palghar-401303'''
print(a)