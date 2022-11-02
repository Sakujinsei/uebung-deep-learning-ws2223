x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [x*2 for x in x]
print (a)

b = [x]
print (b)

c = [y for y in y if y is True or y == "True"]
print (c)

d = [y for y in y if type(y) == str]
print (d)
#I´m sorry but I just don´t quite get what you want for e, so here´s the part I did understand: 

e = [x for x in x if x%2 != 0]
print (e)

print("press enter to exit")
egress = input()
if egress:
 exit(0)

