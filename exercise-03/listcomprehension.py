x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]
a=[2*num for num in x]
b=[num for num in x if num%2==0]
c=[z for z in y if z==True or z=="True"]
d=[z for z in y if type(z)==type("")]
e=[[True for j in range(x[i])] for i in range(len(x)) if i%2==1]


print(a)
print(b)
print(c)
print(d)
print(e)


