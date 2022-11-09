# The file 4.py contains a full python script and can be executed directly. It produces output such as the following:

# 0 25 52 48 61 32 69 28 51 52 50 46 106 26 11 36 58 
# 1 52 54 16 4 25 49 56 99 20 36 25 37 23 62 72 59 39 41 53 53 
# 2 34 49 42 24 67 33 23 64 53 39 39 76 87 31 
# 3 36 18 62 6 39 41 39 34 87 22 26 50 37 78 34 43 49 24 36 38 
# 4 59 46 63 54 69 44 88 92 44 51 62 16 40 42 
# 5 44 67 68 4 83 57 53 69 70 49 
# 6 41 39 52 41 49 49 27 43 45 41 
# 7 37 49 56 52 40 14 
# 8 46 81 55 44 27 54 
# 9 39 38 54 30 37 50 42 33 28 32 35 70 35 39 14 
# The first column of the table is a row number. The remaining columns contain between 5 and 20 normally distributed random numbers. 
# Your goal is to implement a simple padding mechanism. Padding means that we add zeros to each row, such that each row has the same length in the end. 
# Thus, the output of row 0 should be, for instance, 0 25 52 48 61 32 69 28 51 52 50 46 106 26 11 36 58 0 0 0 0.

# Your padding implementation should use exceptions. The idea is to make a for loop until 20, and try to access the list element at the position. 
# If the list is shorter, we catch the exception and print a zero.

# # import random

# # l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

# # i = 0
# # for outerlist in l1:
# #   print(i, end=" ")
# #   for element in outerlist:
# #     print(element, end=" ")
# #   print()
# #   i = i + 1

# except it doesnt. the script given produces results as 
# 0 32 61 62 35 41 40 75 48 42 
# 1 29 30 65 77 75 47 44
# 2 45 46 45 56 27 52 61 28 67 21 46 66
# 3 74 72 69 42 56 23 74 40 52 59 73 54 51 34 73 23 42 49
# 4 27 38 55 35 80 23 64 38 84 61 54 30 48 41 39 59 79 53
# 5 89 40 45 15 35 72 49 20 70 31 31 23 53 62 75
# 6 76 54 7 67 51 44 15
# 7 63 76 63 5 31 61 78 31 61 58 66 75 62 101 34 89 41 37
# 8 71 64 41 69 51 48 48 20 86 24
# 9 -3 41 25 62 70 40 95 25 72 -2 23 46

import random

l1 = [[int(random.normalvariate(50, 20)) for x in range(random.randint(5, 20))] for x in range(10)]

i = 0
for outerlist in l1:
    print(i, end=" ")
    for element in outerlist:
        print(element, end=" ")
    print()
    i = i + 1

rows = 0
for row in l1:
    print(element, end=" ")
    for index in range(20):
        try:
            row[index]
        except IndexError:
            row.append(0)
    for element in row:
        print(element, end=" ")
        print()
        rows = rows + 1