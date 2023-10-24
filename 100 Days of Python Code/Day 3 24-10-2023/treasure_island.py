print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
'''     
)

print("Welcome to the treasure Island! your mission is to find the treasure.")
which_side = input("You are at cross road. where do you want to go? type 'R' for Right, 'L' for Left: ")
selected_side = which_side.lower()
if selected_side == "l":
    swim_or_wait = input("Do you want to swim or wait? type 'S' to swim or 'W' to wait: ")
    select_s_or_w = swim_or_wait.lower()
    if select_s_or_w == "w":
        door = input("Which door you want to select? type 'B' for Blue, 'Y' for yellow, 'R' for Red: ")
        selected_door = door.lower()
        if selected_door == "r":
            print("You are Burned by fire. Game Over!")
        elif selected_door == "b":
            print("Eaten by beasts. Game Over.")
        elif selected_door == "y":
            print("You Win!!")
        else:
            print("Game Over!!")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
