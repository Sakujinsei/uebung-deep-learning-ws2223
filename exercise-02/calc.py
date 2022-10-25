print("Enter number 1:")
num1 = int(input())
print("Enter number 2:")
num2 = int(input())
print ("what should I do with these numbers?: ")
op = str(input())
if op == "add":
 print("Sum: " + str(num1+num2))
elif op == "multiply":
 print("Product: " + str(num1*num2))
else:
 print("I´m sorry Dave, I can´t do that")
print("Press Enter to exit")
a = input()
if a:
 exit(0)
 