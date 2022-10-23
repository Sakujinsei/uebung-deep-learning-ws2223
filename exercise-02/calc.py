row = None
while row is None:
    nummer1 = int(input("Enter number 1: "))
    print(nummer1)
    nummer2 = int(input("Enter number 2: "))
    print(nummer2)

    print("Which operation do you want me to do? ")
    operation = input("Enter + / * or addition / multiplication: ")

    summe = nummer1 + nummer2
    produkt = nummer1 * nummer2

    if operation == "+" or operation == "addition":
        print(f'The sum is {summe}.')
    elif operation == "*" or operation == "multiplication":
        print(f'The product is {produkt}')

    rep = input("Do you wish to continue? y/n: ")
    if rep == "n":
        break
