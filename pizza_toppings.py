pizza = {
    'crest':'thick',
    'toppings':['extra cheese','mushrooms']
}

print("You have ordered " + pizza['crest'].title() + "-crest Pizza. and the toppings are")

for topping in pizza['toppings']:
    print(topping.title())