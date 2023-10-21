print("Welcome to Ding Dong Rollercoaster")
height = int(input("Enter your Height in cm: "))
if height >= 120:
    print("Hi, You can ride the roolercoaster!!")
    age = int(input("Enter your age: "))
    if age <= 18:
        print("Your Ticket Price is $7")
    else:
        print("Your Ticket Price is $12")
else:
    print("Sorry, you have to grow taller before you ride the coaster.")