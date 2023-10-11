users = {
            'aeinstein':{
            'first_name':'albert',
            'last_name':'einstein',
            'location':'princeton'
            },
            'mcurie':{
            'first_name':'marie',
            'last_name':'curie',
            'location':'paris'
            }
        }

for username, user_info in users.items():
    print("User Name : " + username)
    full_name = user_info['first_name'] + " " + user_info['last_name']
    loaction = user_info['location']
    print(full_name.title())
    print("Location is " + loaction.title() + "\n")