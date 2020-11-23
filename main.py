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


#Each of the "while loops" below here contains an input function that takes the number you put in and adds it to a list.
#It will keep adding numbers to the list as you enter them every turn of the loop but as soon as you enter "=" -
#a "for loop" that is inside the "while loop" will start.
#The for loop goes through every number of the list and adds them or subtracts them or multiplies them with each other - 
#depending on the mode you've chosen in the menu. It then spits out the reult from all the numbers in the list. 
#After this point it will wait 2 seconds and thereafter return to the menu and start all over again.
#I hope this comment was helpful to understand the code below. Either way, you are welcome.



#Code for adding numbers. Choice 1.
	if choice == "1":
		print("ADDITION")
		time.sleep(1.5)
		os.system("cls")
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
		print("SUBTRAKTION")
		time.sleep(1.5)
		os.system("cls")
		while True:
			print("Skriv '=' om du är klar")
			print(f"Här är alla talen du lagt till: {list_of_numbers}")
			thing = input(f"Skriv in tal nummer {number_of_numbers}: ")
			thing = thing.replace(thing,f"-{thing}")
			os.system("cls")
			if not thing == "-=":
				list_of_numbers.append(thing)
				number_of_numbers += 1
				os.system("cls")
			else:
				for i in list_of_numbers:
					i = i.replace("-", "")
					number = number - int(i)
				print(f"Den totala differensen av talen är {number}")
				time.sleep(2.5)
				os.system("cls")
				number_of_numbers = 1
				list_of_numbers = []
				number = 0
				break


#Code for multiplying numbers. Choice 3.
	if choice == "3":
		print("MULTIPLIKATION")
		time.sleep(1.5)
		os.system("cls")
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


