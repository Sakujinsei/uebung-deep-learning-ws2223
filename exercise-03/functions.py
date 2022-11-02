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

def func2(*args):
  numArgs = len(args)
  if numArgs < 2:
    return str(numArgs)
  if numArgs == 2:
    return func1(args[0],args[1])
  if numArgs > 2:
    return int(numArgs)

def func3(**args):
 if ("a" and "b") in args :
  return func1(args["a"],args["b"])
 else:
  dicKeys=args.keys()
  return func2(*list(dicKeys))
  
print(func1(1,2))
print(func1("Welt", "Hallo"))
print(func1(None, None))
print(func1(11, "Freunde"))
print(func1(5.4, 3.6))