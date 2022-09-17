# Manipulating numbers and making use of the F string

print(8 / 3)
# regular division

print(int(8 / 3))
# casted float result to whole number by rounding down to nearest whole.

print(round(8 / 3, 0))
# division with rounded up result, the last number is the number of decimal places

print(round(3.14195, 2))

print(8 // 3)
# Rounds down to a whole number

# instead of using concatination , you could use the "F-string"
score = 9
height = 1.8
isWinning = True
print(f'your score is {score}, your height is {height}, and it is {isWinning} that you are winning')