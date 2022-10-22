def calc_function():
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Enter math operation. Either addition or multiplication: ")
    str1 = str(input())
    if str1 == "addition" or str1 == "add":
        print("Sum: " + str(num1+num2))
    elif str1== "multiplication" or str1 == "multi":
        print("Product: " + str(num1*num2))
    else:
        print("That operation was not expected")
    print("Do you want to continue? Type yes to continue")
    str2 = str(input())
    if str2 == "yes":
        calc_function()
        
calc_function()