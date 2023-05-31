motorcycles = ['honda', 'tvs', 'bajaj', 'yamaha']
capitalized_motorcycles = [cycle.title() for cycle in motorcycles]


motorcycles.append('hero')
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle.title())
print(capitalized_motorcycles)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")


