#################### Filip Hedman ####################
    ####Comments are in english. Deal with it.####

#Importing shit.
import os
import time


#Variables
number_of_numbers = 1
list_of_numbers = []
thing = "GoodGameWellPlayed"
number = 0


#Start of loop.
while True:
	print("[1] Räkna med addition")
	print("[2] Räkna med subtraktion")
	print("[3] Räkna med multiplikation")
	print("[4] Avsluta")
	print("[5] Avsluta annorlunda")
	choice = input("")
	os.system("cls")


#Code for adding numbers. Choice 1.
	if choice == "1":
		while True:
			print("Skriv '=' om du är klar")
			print(f"Här är alla talen du lagt till: {list_of_numbers}")
			thing = input(f"Skriv in tal nummer {number_of_numbers}: ")
			os.system("cls")
			if not thing == "=":
				list_of_numbers.append(thing)
				number_of_numbers += 1
				os.system("cls")
			else:
				for i in list_of_numbers:
					number = number + int(i)
				print(f"Summan av talen är {number}")
				time.sleep(2)
				os.system("cls")
				number_of_numbers = 1
				list_of_numbers = []
				number = 0
				break

			
		

#Code for subtracting numbers. Choice 2.
	if choice == "2":
		while True:
			print("Skriv '=' om du är klar")
			print(f"Här är alla talen du lagt till: {list_of_numbers}")
			thing = input(f"Skriv in tal nummer {number_of_numbers}: ")
			os.system("cls")
			if not thing == "=":
				list_of_numbers.append(thing)
				number_of_numbers += 1
				os.system("cls")
			else:
				for i in list_of_numbers:
					number = number - int(i)
				print(f"Differensen av talen är {number}")
				time.sleep(2)
				os.system("cls")
				number_of_numbers = 1
				list_of_numbers = []
				number = 0
				break


#Code for multiplying numbers. Choice 3.
	if choice == "3":
		number = 1
		while True:
			print("Skriv '=' om du är klar")
			print(f"Här är alla talen du lagt till: {list_of_numbers}")
			thing = input(f"Skriv in tal nummer {number_of_numbers}: ")
			os.system("cls")
			if not thing == "=":
				list_of_numbers.append(thing)
				number_of_numbers += 1
				os.system("cls")
			else:
				for i in list_of_numbers:
					number = number * int(i)
				print(f"Summan av talen är {number}")
				time.sleep(2)
				os.system("cls")
				number_of_numbers = 1
				list_of_numbers = []
				number = 0
				break


#Code for exiting the program. Choice 4 and 5.
	if choice == "4":
		print("Avslutar...")
		time.sleep(2)
		os.system("cls")
		break


	if choice == "5":
		print("AVSLUTAR!!!")
		time.sleep(2)
		os.system("cls")
		break


