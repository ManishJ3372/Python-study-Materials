# l1=[22,44,55,66,77]    expected output :second highest element

# l1=[22,44,55,66,77]
# print("Second largest element is:", sorted(l1)[-2])

# create one banking application using encapsulation..and hide some user information.

# def fizz_buzz(numbers):
#     Given a list of integers:
#     1.Replace all integers that are evenly divisible by 3
#     with "fizz"
#     2.Replace all integers divisible by 5 with "buzz"
#     3.Replace all integers that are divisible by  both 3 and 5
#     with "fizzbuzz"
#     >>> numbers = [45,22,14,65,97,72]
#     >>> fizz_buzz(numbers)
#     >>> numbers
#     ['fizzbuzz',22,14,'buzz',97,'fizz']


# for i, num in enumerate(numbers):
#     if num % 3 == 0:
#         numbers[i] = "fizz"
#     if num % 5 == 0:
#         numbers[i] = "buzz"
#     if num % 3 == 0 and num % 5 == 0:
#         numbers[i] = "fizzbuzz"


# lst = [4, -13, 22, 18]
#
#
# def square(x):
#     return x * x


# map(square, lst)
# list(map(square, lst))

# result = []
# for num in lst:
#     result.append(square(num))
# print(result)
# [square(num) for num in lst]
# print(result)

# lst = [1, 2, -5, 4]
#
#
# def is_odd(x):
#     return x % 2 == 1
#
#
# filter(is_odd, lst)
# list(filter(is_odd, lst))
# print([num for num in lst if is_odd(num)])


# num_rows = 2
# num_col = 3
# grid = []
# for _ in range(num_rows):
#     curr_row = []
#     for _ in range(num_col):
#         curr_row.append(0)
#     grid.append(curr_row)
# print(grid)

# grid = [[0 for _ in range(num_col)] for _ in range(num_rows)]
# print(grid)

# print(max(1, 5, 8))

# lst = [12, 23, -65, 49]
# print(max(lst))

# print(max(lst, key=lambda x: x * x))


# print(min(lst))
#
# print(min(lst, key=lambda x: x * x))

# print(any(lst))
# print(any([True, False]))
# print(any([False, False]))
# print(any(lst, key=lambda x: x % 2 == 1))
# print(any([(lambda x: x % 2 == 1)(num) for num in lst]))
# print(all([(lambda x: x % 2 == 1)(num) for num in lst]))

# def max(lst):
#     max_num = -float('inf')
#     for num in lst:
#         breakpoint()
#         if num > max_num:
#             print('entered if statement')
#             max_num = num
#         return max_num
#
#
# print(max([-1, -2, -4]))

# age = 25
# name = "manish"


# print("My name is %s. I am %s years old" % (name, age))
# print("My name is {0}. I am {1} years old".format(name, age))
# print("My name is {name}. I am {age} years old".format(name=name, age=age))

# class A(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         # return f"""
#         #     My name is {self.name}.
#         #     I am {self.age}years old
#         # """
#         return (
#             f"My name is {self.name}."
#             f"I am {self.age} years old"
#         )
#
#
# print(A(name, age))


# animals = ["cat", "dog", "cheetah", "rhino"]
# print(sorted(animals))
# print(sorted(animals, reverse=True))

# animals = [
#     {'type': 'cat', 'name': 'Manish', 'age': 25},
#     {'type': 'dog', 'name': 'Tushar', 'age': 20},
#     {'type': 'rhino', 'name': 'Shubham', 'age': 22},
# ]
# print(sorted(animals, key=lambda animal: animal['age']))
# print(sorted(animals, key=lambda animal: animal['age'], reverse=True))
# print(sorted(animals, key=lambda animal: animal['age'])[0])
# print(animals.sort(key=lambda animal: animal['age']))


# s = set()
# s.add('h')
# s.add('h')
# s.add('i')
# print(s)

# print(set("hello"))

# g = (x for x in [1, 2, 3])
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))


# def f():
#     yield 1
#     yield 2
#     yield 3
# print(f())
#
# g = f()
# print(next(g))
# print(next(g))
# print(next(g))


# student_grades = {"Manish": [85, 90], "Tushar": [80, 95]}
# print(student_grades["Manish"])
#
# print(student_grades.get("Manish", []))
# print(student_grades["Manish"])

# from collections import defaultdict
# d = defaultdict(lambda: 10)
# print(d[5])
#
# d[5] += 10
# print(d[5])

# fname = (input("Enter your first name : "))
# lname = (input("Enter your last name : "))
# print("Hello " + lname + " " + fname)

# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List :', list)
# print('Tuple :', tuple)


