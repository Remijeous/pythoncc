import random

NUM_DIGITS = 3 #(!) Try setting this to 1 or 10.
MAX_GUESSES = 10 # (!) Try setting this to 1 or 100.

def main():
    print(f'''\nI am thinking of a {NUM_DIGITS}-digit number with no repeated digits. Try to guess what it is. Here are some clues:

    When I say: That means:
     Pico One digit is correct but in the wrong position.
     Fermi One digit is correct and in the right position.
     Bagels No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.''')
    while True: #Main game loop
        secretNum = getSecretNum()


def getSecretNum():
    numbers = list('1234567890')
    random.shuffle(numbers)
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[1])

