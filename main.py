from random import randint

dices_number = int(input("How many dices do you want to have?"))

while dices_number >0:
	print(randint(1,6))
	dices_number -=1


