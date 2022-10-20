import calc

print("add/addition or multi/multiplication")
option = str(input())
print("Enter number 1: ")
num1 = int(input())
print("Enter number 2: ")
num2 = int(input())
if option == "add":
        print("Sum: " + str(num1 + num2))
elif option == "addition":
        print("Sum: " + str(num1 + num2))
elif option == "multi":
        print("Product: " + str(num1 * num2))
elif option == "multiplication":
        print("Product: " + str(num1 * num2))
print("would you like to continue?")
option2 = str(input())
if option2 == "yes":
    calc
elif option2 == "continue":
    calc
else:
    exit()