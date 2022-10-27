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
	if len(args) < 2:
		return str(len(args))
	elif len(args) == 2:
		func1(args[0], args[1])
	else:
		return len(args)

def func3(**kwargs):
	l = [kwargs[key] for key in kwargs]
	ab = [ab for ab in l if ab == "a" or ab == "b"]
	if len(ab) == 2:
		func1(ab[0], ab[1])
	else:
		func2(l)

func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)

func2(3, 6, 4)
func2(3,7)
func2("Hans")

func3(a="a", b="b", c="b")
func3(a="n")
func3(a="a", b="b")
