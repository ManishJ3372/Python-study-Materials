# Type Conversion -->the process of converting the value of one data type(in,str,float,...etc)
#two types of type conversion
#1.Implicit Type conversion
#2.Explicit type conversion

#Implicit type conversion-->ptyhon automatically converts one data type to another data type
a=5
b=5.5
c=a+b
print(c)
print(type(c))

a=5
b="python"
c=a*b
print(c)
print(type(c))

#Explicit type conversion--.user convert the data type of an object to required data type
#User convert one data type to another data type(user convert one data type to required data type

a=10 #int
print("before converting",a)
print(type(a))

print("int to float")
a=float(a)
print("after converting",a)
print(type(a))

print("int to string")
a=str(a)
print("after converting",a)
print(type(a))

print("int to boolean")
a=bool(a)
print("after converting",a)
print(type(a))

print("int to complex")
a=complex(a)
print("after converting",a)
print(type(a))