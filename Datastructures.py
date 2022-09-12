# stack = []
# stack.append(1)
# stack.append(2)
#
# pop_elem = stack.pop()
# print(stack,pop_elem)
#
# queue = []
# queue.append(1)
# queue.append(2)
#
# pop_elem = queue.pop()
# print(queue,pop_elem)


# set1 = set[1, 2, 3, 4, 6]
# set2 = set[6, 8, 9, 4, 7]
#
# intersection = set1 & set2
# print(intersection)

# ages = dict()
#
# ages["Manish"] = 25
# ages["Tushar"] = 20
# ages["Sunita"] = 43
# ages["Rakesh"] = 53
#
# for key, value in ages.items():
#
#     print(key, value)
#
# print(ages)

# lst = [1, 2, 3, 4, 5, 6, 7]
#
# even_lst = [x for x in lst if x % 2 == 0]
# print(even_lst)
#
# square_lst = [x ** 2 for x in lst]
# print(square_lst)

# from collections import defaultdict
#
# exam_grades = [("Manish", 60), ("Tushar", 65),
#               ("Sunita", 75), ("Rakesh", 70),
#               ("Shubham", 80)]
#
# students_grades = defaultdict(list)
#
# for name, grade in exam_grades:
#     students_grades[name].append(grade)
#
# print(students_grades)
#
# print(students_grades["Ruchi"])


# from collections import Counter
#
# numbers = [1, 2, 3, 4, 3, 1, 2, 4, 5, 6, 5, 8, 8, 7, 9, 0]
#
# counts = Counter(numbers)
#
# print(counts)
#
# top5 = counts.most_common(5)
# print(top5)

# def grt(a, b, c):
#     return max(a, b, c)
#
#
# print(grt(10, 20, 30))

# case 1
# l = [1, 2, 3, 4]
# ll = [11, 22, 33, 44]
# ln = min(len(l),len(ll))
# if i in range():
# l[i]: ll[i]
# print(d)

# ages = {"manish": 25, "tushar": 20, "sunita": 43}
#
# print(max(zip(ages.values(), ages.keys())))
# print(min(zip(ages.values(), ages.keys())))
