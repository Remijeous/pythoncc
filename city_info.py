"""this program is about print popular ciies in india and interesting this about them"""
popular_cities = {
    'mumbai':{
        'state':'maharastira', 
        'population':'19.98 million', 
        'fact':'financial capital of india'},
    'delhi':{
        'state':'delhi territory',
        'population':'16.31 million',
        'fact':'capital city of india'},
    'bangalore':{
        'state':'karnataka',
        'population':'14.52 million', 
        'fact':'silicon valley on india'}
}

for city, city_info in popular_cities.items():
    print("\nCity Name is " + city.title())
    STATE = city_info['state']
    POPULATION = city_info['population']
    FACT = city_info['fact']
    print("State Name:\t" + STATE.title())
    print("Population:\t" + POPULATION.title())
    print("Fact:\t\t" + FACT.title())
