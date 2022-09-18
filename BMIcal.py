height = input('Enter your height in m : ')
weight = input('Enter your weight in kg : ')

h = float(height)
w = float(weight)
# 
BMI = (w / (h ** 2))

if BMI < 18.5:
    print(f'Your BMI is {BMI}, You\'re Underweight.')
elif BMI < 25:
    print(f'Your BMI is {BMI}, You have a Normal weight.')
elif BMI < 30:
    print(f'Your BMI is {BMI}, You\'re Overweight.')
elif BMI < 35:
    print(f'Your BMI is {BMI}, You\'re Obese.')
else:
    print(f'Your BMI is {BMI}, You\'re Clinically Obese.')

print(BMI)
print(f'Approximately {round(BMI)}')