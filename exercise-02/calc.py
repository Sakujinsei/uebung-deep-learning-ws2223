cont = True


def calculate():
    print("Enter number 1: ")
    num1 = float(input())
    print("Enter number 2: ")
    num2 = float(input())
    print("Enter operation: ")
    op = input()
    if op in ["+", "add", "addition"]:
        result = num1 + num2
    elif op in ["-", "subtract", "subtraction"]:
        result = num1 - num2
    elif op in ["*", "multiply", "multiplication"]:
        result = num1 * num2
    elif op in ["/", "divide", "division"]:
        result = num1 / num2
    else:
        print("Invalid input")
        return True
    if result.is_integer():
        print(int(result))
    else:
        print(result)
    print("Continue?")
    if input() in ["yes", "y"]:
        return True
    else:
        return False


while cont:
    cont = calculate()
