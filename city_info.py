popular_cities = {
    'mumbai':{'state':'maharastira', 'population':'19.98 million', 'fact':'financial capital of india'},
    'delhi':{'state':'delhi territory','population':'16.31 million','fact':'capital city of india'},
    'bangalore':{'state':'karnataka','population':'14.52 million', 'fact':'silicon valley on india'}
}

for city, city_info in popular_cities.items():
    print("\nCity Name is " + city.title())
    state = city_info['state']
    population = city_info['population']
    fact = city_info['fact']
    print("State Name:\t" + state.title())
    print("Population:\t" + population.title())
    print("Fact:\t\t" + fact.title())
