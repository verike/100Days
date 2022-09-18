# Conditional Operators (If Statements & nested If statements)

print('Welcome to a roller coaster')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can ride the roller coaster!')
    age = int(input('Enter your age: '))

    if age < 12:
        print('Please pay $5.')
    elif age <= 18:
        print('Please pay $7.')
    else:
        print('please pay $12.')
else:
    print('You can not ride the roller coaster, because you\'re not yet tall.')


# Check if a number is Odd or Even

# print('Welcome to number checker')

# number = int(input('Enter a number: '))

# test = number % 2

# if test == 0:
#     print('This is an Even Number')
# else:
#     print('This is an Odd Number')