"""This module defines a function to print the favorite languages of a given person."""

fav_places = {
    'rey':['kerala','coimbatore','ooty'],
    'nivi':['kerala','thanjavur','kodaikanal'],
    'joy':['chennai','mumbai','bangalore']
}
for name, places in fav_places.items():
    print("\n" + name.title() + "'s favourite places are: ")
    for place in places:
        print(place.title())
