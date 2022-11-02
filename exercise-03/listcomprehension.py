x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

# A list called `a` that contains all elements of `x`, multiplied by 2.
list_a = [2*x for x in x]
print (list_a)

# A list called `b` that contains all even elements of `x`.
for num in x:
    if num % 2 == 0:
        print(num, end=" ")

# Dies nun als Liste
list_b = [x for x in x if x % 2 == 0]
print (list_b)        

#  A list called `c` that contains all truish elements of `y`
#  (i.e., all elements that evaluate to `True` in a boolean context)
list_c = [y for y in y if y == True]
print (list_c)

# A list called `d` that contains all string elements of `y`
list_d = [y]
print (list_d)

# aber wieso dann nicht einfach
print (y)

# A list called `e` that contains a list for each odd element of `x`.
# The number of list elements is given by the current number of `x`, and all inner list elements are `True`.
# Use I.e., the list `e` starts like this: `[[], [True, True], [True, True, True, True], ...]`
liste_e = [x for x in x if x % 2 == 1]
print (liste_e)