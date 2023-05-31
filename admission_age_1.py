admission_age = 8

if admission_age < 4:
    price = 0
elif admission_age < 18:
    price = 5
else:
    price = 10

print("Your admission fee is $" + str(price) + ".")