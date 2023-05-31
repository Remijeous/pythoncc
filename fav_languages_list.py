fav_languages = {
    'rey':['python', 'kotlin'],
    'vino':['c#','java'],
    'anna':['ruby', 'go'],
    'edward':['haskell']
}

for name, languages in fav_languages.items():
    if len(languages) == 2:
        print("\n" + name.title() + "'s favourute languages are:")
        for language in languages:
            print(language.title())
    else:
        print("\n" + name.title() + "'s favourite language is:")
        print(language.title())