print("Enter number 1: ")
num1 = int(input())
print("Enter number 2: ")
num2 = int(input())
print("What operation do you want to do? (type \"add\" for \"addition\" or \"multi\" for \"multiplication\")")
op = input()
if op == "add":
    print("You chose "+op+". Sum: " + str(num1+num2))
else:
    print("You chose "+op+". Product: " + str(num1*num2))