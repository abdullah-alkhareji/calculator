
def main():
	#write your code here
	firstNumber = input("Enter the first number: ")
	secondNumber = input("Enter the second number: ")
	operation = input("Choose the operation (+, -, /, *): ")

	if firstNumber.isdigit() == False:
		print("The number is invalid")

	elif secondNumber.isdigit() == False :
		print("The number is invalid")
	
	else:
		if operation == "+":
			answer = int(firstNumber) + int(secondNumber)
			print("The Answer: ", answer)
		elif operation == "-":
			answer = int(firstNumber) - int(secondNumber)
			print("The Answer: " , answer)
		elif operation == "/":
			answer = int(firstNumber) / int(secondNumber)
			print("The Answer: " , answer)
		elif operation == "*":
			answer = int(firstNumber) * int(secondNumber)
			print("The Answer: " , answer)
		else: print("Operation is not valid")


	pass
	



if __name__ == '__main__':
	main()
