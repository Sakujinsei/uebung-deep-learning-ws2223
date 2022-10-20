# Quick Calculation Program
def start():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("What operation do you want to do? (type \"add\" \\ \"addition\" or \"multi\" \\ \"multiplication\")")
    op = input()
    if op == "multi" or op == "multiplication":
        print(f"You chose {op}. \nProduct: " + str(num1*num2))
        ask_continue()
    elif op == "add" or op == "addition":
         print(f"You chose {op}. \nSum: " + str(num1+num2))
         ask_continue()
    else:
        print("Sorry, this operation doesn't exist. Try again")
        start()

def ask_continue():
    print("Do you want to play another round?")
    answer = input()
    if answer == "yes" or answer == "ja" or answer == "ya":
        start()
    else:
        exit()

start()