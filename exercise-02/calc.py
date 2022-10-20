while True:
    #Zahlen innput
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    #Rechenoperation
    print("Rechenoperation[+*]")
    op=input()
    if op=="+":
        print("Sum: " + str(num1+num2))
    elif op=="*":
        print("Product: " + str(num1*num2))
    else:
        print("Eingabe fehlerhaft")
    
    #Wiederholung
    print("Neustart?[y/n]")
    ns=input()
    if ns=="n":
        break
    elif ns=="y":
        print("Neustart")
    else:
        print("Eingabe fehlerhaft")