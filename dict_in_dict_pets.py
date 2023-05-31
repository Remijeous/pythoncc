pets = {
    'tom':{'animal_type':'cat','owner_name':'harry'},
'cj':{'animal_type':'dog', 'owner_name':'william'},
'emma':{'animal_type':'cow','owner_name':'peter'}
}

for pet_name, user_info in pets.items():
    print("\nThe name of Pet is: " + pet_name.title())
    print("Type of Animal is: " + user_info['animal_type'].title())
    print("Owner Name of the Animal is: " + user_info['owner_name'].title())