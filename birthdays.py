"""
Program: birthdays.py
Author: Sabrina
Date: 9/11/19

Program will display a  list of names. WHen the user types a valid name, that person's birthday will display, If the user does not enter a valid name, an error will be displayed and they can try again.
"""

# Dictionary object to store the names and associated birthdays
birthdays = {"Albert Einstein":"03/14/1879",
			 "Ben Franklin":"01/17/1706",
			 "Bill Gates":"10/28/1955",
			 "Plato":"424 BC",
			 "Guido Van Rossum":"01/31/1956"}

while True:
	print("Welcome to the birthday directory. We can tell you the birthdays of:")
	print()
	# The for loop counter refers to the keys of the dictionary
	# The loop will print the names of the people only
	for name in birthdays:
		print(name)

	person = input("Which person do you want to know the birthday of? >>> ")

	if person in birthdays:
		print("The birthday for " + person + " is " + birthdays[person])
		print()
	elif person.upper() == "QUIT":
		print()
		print("Later alligator!")
		break
	else:
		print("Sorry, " + person + " is not in our database. Try again. ")
		print("\n\n")
