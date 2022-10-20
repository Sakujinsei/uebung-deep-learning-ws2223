running = True
while(running):
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Decide if you want to do addition or multiplication. /nEnter [+/addition/add, */multiplication/mult]")
    query_answer = input()
    addition = query_answer == "addition" or query_answer == "add" or query_answer == "+"
    multiplication = query_answer == "multiplication" or query_answer == "mult" or query_answer == "*"
    if (addition):
        print("Sum: " + str(num1+num2))
    elif (multiplication):
        print("Product: " + str(num1*num2))
    print("Continue? [Yes/No]")
    continuation_answer = input()
    if (continuation_answer == "Yes" or continuation_answer == "yes" or continuation_answer == "y"):
        pass
    else:
        running = False
