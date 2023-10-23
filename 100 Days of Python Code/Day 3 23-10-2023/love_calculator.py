print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")

name = name1 + name2
lower_name = name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_digit = t + r + u + e
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_digit = l + o + v + e
love_score = str(first_digit) + str(second_digit)

love_score = str(first_digit) + str(second_digit)
score_integer = int(love_score)
if (score_integer < 10) or (score_integer > 90):
  print(f"Your score is {score_integer}, you go together like coke and mentos.")
elif (score_integer > 40) and (score_integer < 51):
  print(f"Your score is {score_integer}, you are alright together.")
else:
  print(f"Your score is {score_integer}.")