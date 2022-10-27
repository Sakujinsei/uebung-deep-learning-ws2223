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
    if (len(args) < 2):
        return f"There are {len(args)} arguments. "
    if (len(args) == 2):
        func1(**args)
    if (len(args) > 2):
        return len(args)


def func3(**kwargs):
    if (kwargs.get('a') and kwargs.get('b')):
        func1(**kwargs)
    else:
        func2(kwargs.values())

func2(2)

func2(2,3,4,5)

func3(a=3, b=5)
func3(s=3, c=5)

