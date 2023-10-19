living_years = 90
current_age = int(input("Enter your Current age in years: "))
years_left = living_years - current_age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {months_left} months or {weeks_left} weeks or {days_left} days left in your life.")