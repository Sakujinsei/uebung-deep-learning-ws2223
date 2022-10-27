def func1(a, b):
  if type(a) == int and type(b) == int:
    # print("if1")# test purpose
    return a+b
  if type(a) == str and type(b) == str:
    # print("if2")# test purpose
    return b+" "+a
  if a is None and b is None:
        # print("if2")# test purpose
        return "Does not exist."
  if type(a) != type(b):
        # print("if2")# test purpose
        return None
  # print("func1")# test purpose
  return type(a)

func1(1,2) # -> returns 3
func1("Welt", "Hallo") # -> returns "Hallo Welt"
func1(None, None) # -> returns "Does not exist."
func1(11, "Freunde") # -> returns None
func1(5.4, 3.6) # -> returns <class 'float'>

def func2(*args):
    if len(args) < 2:
      # print("func2 if1")# test purpose
      return str(len(args))
    if len(args) == 2:
      # print("func2 if2")# test purpose
      return func1(args[0], args[1])
    else:
      # print("func2 if3")# test purpose
      return len(args)

print(func2(3,4)) # Test purpose
# print(type(func2(3,))) # -> Test: should return <class 'str'>

# write a function func3 that takes an arbitrary number of named arguments. 
# Check that two of these arguments have the names a and b. 
# If so, pass them into func1. If not, pass all names of the arguments into func2.
def func3(**kwargs):
  for key in kwargs:
    if key == "a" and key == "b":
      # print("func3.1")# test purpose
      return func1("a","b")
    else:
      # print("func3.2") # test purpose
      return func2(kwargs[key])

print(func3(a="e",b="d")) # test purpose

