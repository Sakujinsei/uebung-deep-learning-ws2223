def calc():  #function
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    print("What do you want to do with these numbers? Enter add/addition or multi/multiplication!")
    choice = input()
    if choice == "add" or choice == "addition":
        print("Sum: " + str(num1+num2))
    elif choice == "multi" or choice == "multiplication":
        print("Product: " + str(num1*num2))
    else:
        print("You didn't enter add/addition or multi/multiply :( Or did you make a spelling mistake?")
    
    print("Do you want to continue? Enter yes or no")
    if input() == "yes":
        calc()
    else:
        exit()
        
calc() #calling the function