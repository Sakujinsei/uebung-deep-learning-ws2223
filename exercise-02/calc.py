def interact():
	print("Enter number 1: ")
	num1 = int(input())
	print("Enter number 2: ")
	num2 = int(input())

	print("Choose operation: add or multiply?")
	answer = input()
	if answer == "add" or answer == "addition" or answer == "Add" or answer == "Addition":
		print("Sum: " + str(num1+num2))
	elif answer == "multiply" or answer == "multiplication" or answer == "Multiply" or answer == "Multiplication":
		print("Product: " + str(num1*num2))
	else:
		print("Invalid operation!")

	print("Continue? Yes/No?")
	if input() == "Yes":
		interact()


interact()