#################### Filip Hedman ####################

#Importing shit.
import os
import time


#Start of loop.
while True:
	print("[1] Räkna med addition")
	print("[2] Räkna med subtraktion")
	print("[3] Räkna med multiplikation")
	print("[4] Avsluta")
	print("[5] Avsluta Annorlunda")
	choice = input("")
	os.system("cls")

#Code for adding numbers. Choice 1.
	if choice == "1":
		tal1 = input("Skriv in tal 1: ")
		os.system("cls")
		tal2 = input("Skriv in tal 2: ")
		os.system("cls")
		print(f"Summan av {tal1} och {tal2} är {int(tal1) + int(tal2)}")
		time.sleep(2)
		os.system("cls")


#Code for subtracting numbers. Choice 2.
	if choice == "2":
		tal1 = input("Skriv in tal 1: ")
		os.system("cls")
		tal2 = input("Skriv in tal 2: ")
		os.system("cls")
		print(f"Differencen mellan {tal1} och {tal2} är {int(tal1) - int(tal2)}")
		time.sleep(2)
		os.system("cls")


#Code for multiplying numbers. Choice 3.
	if choice == "3":
		tal1 = input("Skriv in tal 1: ")
		os.system("cls")
		tal2 = input("Skriv in tal 2: ")
		os.system("cls")
		print(f"Produkten av {tal1} och {tal2} är {int(tal1) * int(tal2)}")
		time.sleep(2)
		os.system("cls")



#Code for exiting the program. This code is active when choice 4 or 5 is chosen.
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



