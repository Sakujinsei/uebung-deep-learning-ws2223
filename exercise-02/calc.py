def func(sum): + str(num1+num2)
def func(pro): + str(num1*num2)


start: print("Enter number 1: ")
num1 = int(input())
print("Enter number 2: ")
num2 = int(input())
give = input("sum or pro")
if sum:
    print("sum: " + str(num1+num2))
elif pro:
    print("pro: " + str(num1*num2))

answer = input ('you want to exit?: [y/n]')
if answer[0].lower() == 'n':
    print("Restart")
    print("Enter number 1: ")
    num1 = int(input())
    print("Enter number 2: ")
    num2 = int(input())
    give = input("sum or pro")
    if sum:
        print("sum: " + str(num1+num2))
    elif pro:
        print("pro: " + str(num1*num2))

if answer[0].lower == 'y':
    exit()
# for yes in range(0, 0):
 #   print("sorry" + exit())
