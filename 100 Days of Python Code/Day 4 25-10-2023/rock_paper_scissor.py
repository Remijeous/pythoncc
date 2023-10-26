import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

ascii_arts = [rock, paper, scissors]
user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(ascii_arts[user_choice])
computer_choice = random.randint(0,2)
print(f"Computer Chooses: {computer_choice}")
print(ascii_arts[computer_choice])


if user_choice == 0:
    if computer_choice == 2:
        print("You win!")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("It's a tie!")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 2:
        print("You lose!")
    else:
        print("It's a tie!")
elif user_choice == 2:
    if computer_choice == 1:
        print("You win!")
    elif computer_choice == 0:
        print("You lose!")
    else:
        print("It's a tie!")
else:
    print("Invalid choice!")
