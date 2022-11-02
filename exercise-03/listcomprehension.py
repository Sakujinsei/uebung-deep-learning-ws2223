x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [x*2 for x in x]    # all elements of x, multiplied by 2
print(a)

b = [x for x in x if x % 2 == 0] #all even elements of x
print(b)

c = [y for y in y if y == True] #all elements that evaluate to True in a boolean context of y
print(c)

d = [y for y in y if type(y) == str]   #all string elements of y
print(d)

e = [[True]*x for x in x if x % 2 != 0] #a list for each odd element of x. The number of list elements is given by the current number of x, and all inner list elements are True
print(e)