weight = float(input("Enter your Weight in Kg's: "))
height = float(input("Enter your Height in m's: "))

bmi = float(weight / height ** 2)
bmi_as_int = int(bmi)
print(bmi_as_int)