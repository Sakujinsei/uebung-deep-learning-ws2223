class Calculator:

    def calculate(self):
        print("which mathematical operation do you want to perform? ")
        op = ""
        op = str(input())
        print("Enter number 1: ")
        num1 = int(input())
        print("Enter number 2: ")
        num2 = int(input())
        print(op)
        if (op == '+') or (op == 'addition'):
            print("Sum: " + str(num1+num2))
        elif (op == '*') or (op == 'multiplication'):
            print("Product: " + str(num1*num2))
        else:
            print("not valid!")
        print("would you like to perform another operation?")
        answer = str(input())
        print(answer)
        if answer == 'y':
            cal.calculate()
cal = Calculator()
cal.calculate()

