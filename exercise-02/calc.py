add = 'add'
multiply = 'multiply'
yes = 'yes'
no = 'no'

while True:
    print("Do you want to add or multiply?")
    input1 = str(input())
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    if input1 == add:
        print("Sum: " + str(num1+num2))

    elif input1 == multiply:
        print("Product: " + str(num1*num2))

    else:
        print("Invalid input! Try 'add' or 'multiply'.")
        break

    print("Do you want to continue?")
    input2 = str(input())

    if input2 == yes:
        continue
    elif input2 == no:
        break
    
