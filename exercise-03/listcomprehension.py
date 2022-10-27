
x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [x*2 for x in x]
print(a)

b = [x for x in x if x%2==0]
print(b)

c = [y for y in y if y==True]
print(c)

d = [y for y in y if isinstance(y,str)]
print(d)

e = [[True for z in range(x-1)] for x in x if x%2==1]
print(e)

#- A list called `a` that contains all elements of `x`, multiplied by 2.
#- A list called `b` that contains all even elements of `x`.
#- A list called `c` that contains all truish elements of `y` (i.e., all elements that evaluate to `True` in a boolean context)
#- A list called `d` that contains all string elements of `y`
#- A list called `e` that contains a list for each odd element of `x`. The number of list elements is given by the current number of `x`, and all inner list elements are `True`. Use I.e., the list `e` starts like this: `[[], [True, True], [True, True, True, True], ...]`