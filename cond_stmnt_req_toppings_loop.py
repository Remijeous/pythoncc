requested_toppings = ['extra cheese', 'pepperoni', 'mushrooms', 'flakes']

for requested_topping in requested_toppings:
    if requested_topping == 'pepperoni':
        print("Pepperoni is out of stock")
    else:
        print("Adding " + requested_topping + ".")

print("finished making your Pizza")