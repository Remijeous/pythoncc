print("Welcome to Ding Dong Rollercoaster")
height = int(input("Enter your Height in cm: "))
if height >= 120:
    print("Hi, You can ride the roolercoaster!!")
    age = int(input("Enter your age: "))
    if age <=12:
        bill = 5
        print("Your Ticket Price is $5")
    elif age < 18:
        bill = 7
        print("Your Ticket Price is $7")
    else:
        bill = 12
        print("Your Ticket Price is $12")

    photo_taken = input("You want to take photo? Type 'Y' for Yes and or'N' for No: ")
    if photo_taken == "Y" or "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you ride the coaster.")