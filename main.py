#################### Filip Hedman ####################

#Importing shit.
import os
import time


#Variables
number_of_numbers = 0


#Start of loop.
while True:
	print("[1] Räkna med addition")
	print("[2] Räkna med subtraktion")
	print("[3] Räkna med multiplikation")
	print("[4] Räkna med divition")
	print("[5] Avsluta")
	choice = input("")
	os.system("cls")

#Code for adding numbers. Choice 1.
	if choice == "1":
		tal1 = input("Skriv in tal 1: ")
		os.system("cls")
		tal2 = input("Skriv in tal 2: ")
		os.system("cls")
		print(f"Summan av {tal1} och {tal2} är {float(tal1) + float(tal2)}")
		time.sleep(2)
		os.system("cls")


#Code for subtracting numbers. Choice 2.
	if choice == "2":
		tal1 = input("Skriv in tal 1: ")
		os.system("cls")
		tal2 = input("Skriv in tal 2: ")
		os.system("cls")
		print(f"Differencen mellan {tal1} och {tal2} är {float(tal1) - float(tal2)}")
		time.sleep(2)
		os.system("cls")


#Code for multiplying numbers. Choice 3.
	if choice == "3":
		tal1 = input("Skriv in tal 1: ")
		os.system("cls")
		tal2 = input("Skriv in tal 2: ")
		os.system("cls")
		print(f"Produkten av {tal1} och {tal2} är {float(tal1) * float(tal2)}")
		time.sleep(2)
		os.system("cls")



#Code for multiplying numbers. Choice 3.
	if choice == "4":
		tal1 = input("Skriv in tal 1: ")
		os.system("cls")
		tal2 = input("Skriv in tal 2: ")
		os.system("cls")
		print(f"Kvoten av {tal1} och {tal2} är {float(tal1) / float(tal2)}")
		time.sleep(2)
		os.system("cls")

	if choice == "5":
		print("Avslutar...")
		time.sleep(2)
		os.system("cls")
		break



