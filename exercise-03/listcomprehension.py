x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]
a = [z*2 for z in x]
b = [z for z in x if ((z % 2) == 0)]
c = [z for z in y if z]
d = [z for z in y if isinstance(z, str)]
print(d)