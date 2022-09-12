# operators-->operators is a symbol that performs certain operation
# two or more then two operand using performs operation

# 1.arithmetic operator
# 2.relational operator
# 3.locical operator
# 4.assignment operator
# 5.bitwise operator
# 6.special operators

# arithmetic operator(+,-,*,/,%,//,**)

# A = 10
# B = 20
# C = A + B
# print(C)
# print("addition", A + B)
# print("subraction", A - B)
# print("multiplacation", A * B)
# print("division", A / B)
# print("remainder", A % B)
# print("float division", A // B)
# print("exponential", A ** B)

# relational operator(<,>,<=,>=,<==,>==)

# a = 10
# b = 5
# print("A less then B", a < b)
# print("A greater then B", a > b)
# print("A less then equals B", a <= b)
# print("A greater than equals B", a >= b)

# logical operator (and,or,not)
# a = 10
# b = 20
# c = 25
# print(a != b and 10 < 5)  # all true (and)
# print(5 == 5 and 5 < 3 and 5 != 4)
# print(a < b and b < c and c > a)
#
# print(a == b or a > b or c < a)  # any one true (or)
# print(a != b or a < b or c > a)
#
# print(not a > b)  # reverse values (not)
# print(not b == a)
# print(not c < a)

# assignment operator (+=,-=,/=,*=,%=,=,|=,&=,^=)
a = 20
b = 80
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a %= b
print(a)

# bitwise operator(binary) (&(and),^(xor),|(not),~(not),>>(right shift),<<(left shift))
# bitwise
# & if both bits are 1 then only result is 1 otherwise 0
# | if atleast one bits is 1 then result is 1 otherwise 0
# ^ if both bits are different then only result is 1 otherwise 0
# ~ use formula -(1+use take numbers)
# >> bitwise left shift operator
# << bitwise right shift operator


# a = 5
# b = 7
# c = a & b
# print(c)
# c = a ^ b
# print(c)
# c = a | b
# print(c)
# c = a >> b
# print(c)
# c = a << b
# print(c)
# a = ~-20
# print(a)

# special operator
# python defines the following 2 special operators
# 1.identify operator
# 2.membership operator

# identity operator(is,is not)
# we can use idetity operator for address comparasion

# a = 5
# b = 5
# print(id(a))
# print(id(b))
# print(a is b)
# print(a is not b)

# membership operator(in,not in)
# we can use menbership operator to check whether the given object is present in the given collection

# a = "python"
# b = "yo"
# print(a in b)
# print(a not in b)
#
# print("java python" in "java")
#
# print("java" in "python")
#
# print("a" in "java")
#
# print("ptyhon" not in "a")
