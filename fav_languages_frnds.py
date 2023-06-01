fav_languages = {
    'rey' : 'python',
    'jim' : 'c++',
    'stuart' : 'Java',
    'max' : 'kotlin'
}

friends = ('jim', 'max')

for name in fav_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + "!, I saw your favourite language is " + fav_languages[name].title())

