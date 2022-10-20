while True:
    print("Do you want to add or multiply?")
    input = str(input())
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    if input == add:
        print("Sum: " + str(num1+num2))

    elif input == multiply:
        print("Product: " + str(num1*num2))

    print("Do you want to continue?")
    input2 = str(input())

    if input2 == yes:
        continue
    elif input == no:
        break
    
