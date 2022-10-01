
# Prompt user and accept integer input

n = input('Enter Year : ')
n = int(n)

if (n % 4) == 0:

    if (n % 100) == 0:

        if (n % 400) == 0:
            print(f'{n} is a Leap Year!')

        else:
            print(f'{n} is not a Leap Year!, Try a different Year.')    
    else:
        print('Not a leap year')

else:
     print(f'{n} is not a Leap Year!, Try a different Year.')