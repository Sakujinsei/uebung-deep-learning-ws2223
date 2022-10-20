def rechnen():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Which kind of mafs operation do you wanna use? [sum / product]")
    op = str(input())

    if op == "sum"or op =="add" or op =="+":
        print("Sum: " + str(num1+num2))

    elif op =="product"or op =="multiplication" or op =="*" or op =="multi" or op == "x":
        print("Product: " + str(num1*num2))

    else:
        print("Error bibabibup")

    print("Wanna do it again [yes,no]?")

    lw = input().lower()
    
    if lw == "true" or lw =="yes"or lw =="y":
        rechnen()

    else:
        quit()

rechnen()

