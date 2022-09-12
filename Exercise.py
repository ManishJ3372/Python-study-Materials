# 1. WAP to check whether given number is prime or not

# A prime number is a natural number greater than 1
# that has no positive divisors other than 1 and itself.
# The first few prime numbers are {2, 3, 5, 7, 11, ….}.


num1 = int(input("Enter the number : "))
if num1 > 1:
    for i in range(2, int(num1 / 2) + 1):
        if (num1 % i) == 0:
            print(num1, "is not a prime number")
            break
    else:
        print(num1, "is a prime number")

else:
    print(num1, "is not a prime number")


# 2. WAP to check palindrome for string and number both

# A palindrome is a number or letter that
# remains the same even if the number and letters are inverted.
# For example:
# 121, 11, 414, 1221, 74747 are the palindrome numbers.
# MOM, DAD, MADAM, REFER are the palindrome letters.
# JAVATPOINT, PROGRAM, JAVA are not the palindrome letters.

string = (input("Enter a string : "))
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("the string is not a palindrome")


num = int(input("Enter a number : "))
temp = num
rev = 0
while (num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if (temp == rev):
    print("This is a palindrome number!")
else:
    print("This is not a palindrome number! ")


# 3. WAP to check given value(string to number) is armstrong or not

# A positive integer is called an Armstrong number of order n if
# In case of an Armstrong number of 3 digits,
# the sum of cubes of each digit is equal to the number itself

num = int(input("Enter a number : "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")

# 4.WAP of fibonacci series
#
# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
#
# The first two terms are 0 and 1.
# All other terms are obtained by adding the preceding two terms.
# This means to say the nth term is the sum of (n-1)th and (n-2)th term.

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(9))











