x= "yes"
while x == "yes":
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("multiply or add?: ")
    operation = input()

    if(operation == "multiply" or operation == "multi" or operation == "*"):
        print("Product: ", str(num1*num2))
    if(operation == "add" or operation == "addition" or operation == "+"):
        print("Sum: " + str(num1+num2))
    print("want to continue? yes/no: ")
    x = input()
