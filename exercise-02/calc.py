conti = "yes"
while conti == "yes":
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter mathematical operation (addition or multiplication)")
    operation = input()

    if operation == "multiply" or operation == "*" or operation == "multi":
        print("Product:" + str(num1 * num2))
    if operation == "add" or operation == "+" or operation == "addition":
        print("Sum: " + str(num1 + num2))
    print("Would you like to continue? Please type yes or no:")
    conti = input()
