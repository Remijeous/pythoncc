users_list = ['adam', 'tesla', 'admin', 'peter', 'ben']

for user in users_list:
    if user == 'admin':
        print("Hello Admin, do you want to generate the report?")
    else:
        print("Hello " + user.title() + ", Thank you for login again")


