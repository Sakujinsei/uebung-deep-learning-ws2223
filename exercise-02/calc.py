s = "yes"
while s == "yes":
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter a math operation add/multiply: ")
    calc = input()

    if calc == "add" or calc == "+" or calc == "addition":
        sumAdd = num1 + num2
        print("Sum: " + str(sumAdd))
    elif calc == "multi" or calc == "*" or calc == "multiply":
        sumMulti = num1 * num2
        print("Product: " + str(sumMulti))

    print("Do you want to play again? Type: yes or no")
    s = input()