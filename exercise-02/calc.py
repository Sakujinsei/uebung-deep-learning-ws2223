def calculator():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    print("Choose operation: addition or multiplication")
    op = input()
    if op == "add" or op == "addition":
        print("Sum: " + str(num1+num2))
    elif op == "multi" or op == "multiplication":
        print("Product: " + str(num1*num2))
    else:
        print("invalid input")
    print("Do you want to continue? type yes or no")
    if input() == "yes":
        calculator()
    else:
        exit()


calculator()