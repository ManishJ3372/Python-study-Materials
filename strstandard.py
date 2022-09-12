# string stander data type
# 1.sequence of characters
# 2.immutable
# 3.represents with the (" ") or (' ') or (''' ''')
# 4.insertion order follows
# 5.indexing

# s = "ptyhon"
# print(id(s))
# print(type(s))
# print(len(s))
# print(s[1:3:1])  # slicing string
# print(s)

# removing spaces form the string
# we can use the following 3 methods
# rstrip()-->to remove space at right hand side
# lstrip()-->to remove space at left hand side
# srtip()-->to remove space both sides

# a="Manish Rakesh Jakhmola"
# a1=a.rstrip()
# print(a1)
# a2=a.lstrip()
# print(a2)
# a3=a.strip()
# print(a3)

# finding substring
# find(substring)
# index(substring)

# splitting of string
# we can split the given string according to specified by using

# a="quastech python java"
# s1=a.split()
# print(s1)
# s="1 2 3 4 5 6 7 8"
# s2=s.split()
# print(s2)


# to check type of characters in a string
# python contains the following method for this purpose
# 1.isalnum()-->returns true if all characters ar alphanumeric
# 2.isalpha()-->returns true if all characters are alphabet symbol
# 3.isdigit()-->returns true if all charachters ar digit only
# 4.islower()-->returns true if all characters are lower case aplhabet
# 5.isupper()-->returns true if all characters are upper case aplhabet
# 6.istitle()-->returns true if string is in title case
# 7.isspace()-->returns true if string contains only space


# isalnum
# print("quastech123".isalnum()) #true
# print("python".isalnum())
# print("1234".isalnum())
# print("@3".isalnum())
#
# #isalpha
# print("Manish".isalpha())
# print("123Manish".isalpha())
# print("@12312".isalpha())
#
# #isdigit
# print("1234".isdigit())
# print("Manish4234".isdigit())
# print("21313@0".isdigit())
#
# #islower
# print("manish".islower())
# print("123manish".islower())
# print("Manish".islower())
#
# #isupper
# print("MANISH".isupper())
# print("Manish".isupper())
# print("123Manish".isupper())
#
# #istitle
# print("Rakesh".istitle())
# print("Java".istitle())
# print("ptyhon".istitle())
#
# #isspace
# print(" Java".isspace())
# print("pyt hon".isspace())
# print("   ".isspace())


# checking starting and ending part od the string
# startswith(substring)
# endswith(substring)

# print("welcome to the python world".startswith("welcome"))
#
# s = "python java django"
# s1 = s.startswith("java")
# print(s1)
#
# s1 = s.endswith("django")
# print(s1)
# s2 = s.endswith("python")
# print(s2)
