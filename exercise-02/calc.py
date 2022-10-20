def calc():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter the math operation: ")
    math_op = input().lower()

    if math_op == "+" or math_op == "add" or math_op == "addition":
        print("Sum: " + str(num1+num2))
    elif math_op == "*" or "multi" or "multiplication":
        print("Product: " + str(num1*num2))
    else:
        print("Can't do this math operation")
    
    print("Want to continue?")
    cntn = input().lower()

    if cntn == "yes" or cntn == "y":
        calc()

if __name__ == "__main__":
    calc()
