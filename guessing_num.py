from random import randint
from IPython.display import clear_output
guessed = False
number = randint(1,100)
guesses = 0
while not guessed:
    ans = input("Try to Guess the number am thinking of!")
    guesses += 1
    clear_output( )

    if int(ans) == number:
        print("Congrats! You Guessed it Correctly.")
        print("it took you {} guesses!".format(guesses))
        break
    elif int(ans) > number:
        print("The number is lower than what you guessed.")
    elif int(ans) < number:
        print("The number is greater than what you guessed")
