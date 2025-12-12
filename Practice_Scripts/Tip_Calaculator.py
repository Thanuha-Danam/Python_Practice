'''
This script will calculate the Tip and split the total bill between the people.

'''

print("Welcome to the Tip Calculator!")
bill = float((input("What is the total Bill amount?\n")))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
no_of_persons = int(input("How many persons will split the bill?\n"))

tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / no_of_persons

print(f"Each person should pay {bill_per_person:.2f}")
