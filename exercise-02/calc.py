def calculator():

    print("What kind of calculation do you want to do? Choose either >> addition << or >> multiplication << ")
    choice = str(input())

    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())

    if choice == "add" or choice == "addition":
        print("Sum: " + str(num1+num2))
    if choice == "multi" or choice == "multiplication":
        print("Product: " + str(num1*num2))
    else:
        print("Calculation not possible.")

    print("Do you want to start over? Enter >> yes << or >> no <<: ")
    choice2 = str(input())
    if choice2 == "yes" or choice2 == "Yes" or choice2 == "okay":
        calculator()

calculator()