while True:
    year = input("Enter the year you want to check (type 'exit' to quit): ")

    if year == 'exit':
        break
    try:
        year = int(year)
    except ValueError:
        print("Invalid input. Please enter a valid year or type 'exit' to quit.")
        continue

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")