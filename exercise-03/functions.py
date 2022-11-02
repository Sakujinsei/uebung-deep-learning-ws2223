def func1(a, b):
  if type(a) == int and type(b) == int:
    return a+b
  if type(a) == str and type(b) == str:
    return b+" "+a
  if a is None and b is None:
    return "Does not exist."
  if type(a) != type(b):
    return None
  return type(a)

def func2(*arg):
    numberOfArgs = len(arg)
    print("Laenge von Arg: ", numberOfArgs)
    if numberOfArgs < 2:
        return "Number of Arguments " + numberOfArgs
    if numberOfArgs > 2:
        return numberOfArgs
    if numberOfArgs == 2:
        return func1(arg[0], arg[1])

print(func1(1,2))
print(func1("Welt", "Hallo"))
print(func1(None, None))
print(func1(11, "Freunde"))
print(func1(5.4, 3.6))
print(func2(6, 5))