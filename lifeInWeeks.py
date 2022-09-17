age = input('Enter your Age : ')
age_in_int = int(age)

years_remaining = 90 - age_in_int

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f'Number of Years remaining is {years_remaining},\n the number of months remaining is {months_remaining},\n the number of weeks remaining is {weeks_remaining}\n and the number of days remaining is {days_remaining}')