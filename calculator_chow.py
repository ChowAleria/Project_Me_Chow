#Aleria, Madel S.

while True:
	print("1.Addition")
	print("2.Subtraction")
	print("3.Multiplication")
	print("4.Division")
	print("5.Exit")
	choice=int(input("Enter your choice:"))
	if (choice>=1 and choice<=4):
		print("Enter two numbes:")
		calcu1=int(input())
		calcu2=int(input())
		if choice == 1:
			res = calcu1+calcu2
			print("Result =", res)
		elif choice == 2:
			res = calcu1-calcu2
			print("Result =", res)
		elif choice == 3:
			res = calcu1*calcu2

			print("Result =",res)
		else:
			res = calcu1/calcu2
			print("Result =",res)
	elif choice ==5:
		break
	else:
		print("Wrong input!")
