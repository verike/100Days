height = input('Enter your height in m : ')
weight = input('Enter your weight in kg : ')

h = float(height)
w = float(weight)
# 
BMI = (w / (h ** 2))
print(BMI)
print(f'Approximately {int(BMI)}')