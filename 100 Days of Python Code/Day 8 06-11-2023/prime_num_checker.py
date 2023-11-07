def prime_checker(number): #This function takes an integer number as input.
  is_prime = True #initializes a variable is_prime to True, assuming the number is prime initially.
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.") 

    

n = int(input("Enter a number: "))
prime_checker(number=n)