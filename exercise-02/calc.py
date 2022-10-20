print("Enter number 1: ")
num1 = int(input())
print("Enter number 2: ")
num2 = int(input())
print("Choose an Operator (+,*): ")
ch = input()
if ch=='+':
    print("\n" +str(num1)+ " + " + str(num2)+ " = " +str(num1+num2))
elif ch=='*':
    print("\n" +str(num1)+ " * " + str(num2)+ " = " +str(num1*num2))  
 

print("Would you like to continue? Y/N")
co = input()
if co=='Y':
    print("Ok, so here we go again!")
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    print("Choose an Operator (+,*): ")
    ch = input()
    if ch=='+':
        print("\n" +str(num1)+ " + " + str(num2)+ " = " +str(num1+num2))
    elif ch=='*':
        print("\n" +str(num1)+ " * " + str(num2)+ " = " +str(num1*num2))
        
elif co=='N':
    print("Ok, Bye!")