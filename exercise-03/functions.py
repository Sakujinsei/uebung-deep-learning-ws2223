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

func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)

def func2(*args):
  if len(args) <= 2:
    return str(len(args))
  if len(args) == 2:
    func1(args)
  else:
    return int(len(args))

print(func2("miau", "si", "no"))
print(func2(5))
print(func2(5, 5))

def func3(*args):
  if args.name == "a" and "b":
    func1()
  else:
    func2()

print(func3(a="Katze", b="Bobby"))