# take input from the user
print("Enter number 1: ")
num1 = int(input())
print("Enter number 2: ")
num2 = int(input())

while True:
    print("Enter any operator")
    choice = input()

    # checks if choice is one of the options
    if choice in ('+', '-', '*', '/', 'add','sub','multi','div', 'addition','substraction','multiplication','devision'):



    
        #addition
        if choice == '+' or choice == 'add' or choice == 'plus' or choice == 'addition':
            print("Sum: " + str(num1+num2)) 


        #substraction
        elif choice == '-' or choice ==  'sub' or choice == 'minus' or choice == 'substraction':
            print("Diff: " + str(num1-num2)) 

        #multiplication
        elif choice == '*' or choice ==  'multi' or choice == 'multiply' or choice ==  'multiplication' :
            print("Product: " + str(num1*num2)) 

        #division 
        elif choice == '/' or choice == 'div' or choice == 'divide' or choice == 'division':
            print("Quot:" + str(num1/num2))   


        # check if user wants another calculation
        # break the while loop if answer is no
        more_math = input("Continue? (yes/no): ")
        if more_math == "no":
            break

    else:
        print("Invalid Input")