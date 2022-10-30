x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]
a = [a1*2 for a1 in x]
print(a)
b = [b1 for b1 in x if b1 % 2 == 0]
print(b)
c = [c1 for c1 in y if c1 == True]
print(c)
d = [d1 for d1 in y if isinstance(d1, str)]
print(d)
e = [[True] * e1 for e1 in x if e1 % 2 != 0]
print(e)

