print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill amount: "))
tip = int(input("What percentage tip would you like to give: "))
total_persons = int(input("How many people to split the bill:  "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill_amount = bill + total_tip_amount
bill_per_person = total_bill_amount / total_persons

print(f"each person should pay {bill_per_person:.2f}")

print(f"Total bill amount to pay is: ${total_bill_amount:.2f}")