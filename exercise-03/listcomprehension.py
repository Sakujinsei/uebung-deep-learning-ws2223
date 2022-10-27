x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [el*2 for el in x]
print(a)

b = [el for el in x if el % 2 == 0]
print(b)

c = [el for el in y if el == True]
print(c)

d = [el for el in y if isinstance(el, str) == True]
print(d)

e = [[True for innerEl in range(el)] for el in x if el % 2 != 0]
print(e)

