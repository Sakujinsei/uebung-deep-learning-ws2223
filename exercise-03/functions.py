from asyncio.windows_events import NULL
from calendar import c
from contextlib import nullcontext


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

def func2():
  print ("Hello, give me a few things you would like to have added. Press the q key when you are done")
  c = list( input().split())
 
  if len(c) < 2:
     return(len(c))
  elif len(c) == 2:
    func1(*c)
  elif len(c) > 2:
    return(len(c))
  else:
    return(None)

func2()

def func3():

 d =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "a": 4,
  "b": 7
}
 if "a" in d and "b" in d:
  func1("a","b")
 else:
  func2(*d)



print("press enter to exit")
egress = input()
if egress:
 exit(0)
