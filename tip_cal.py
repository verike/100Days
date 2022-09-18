# This calculator is used to calculate the percentage tip given to a person probably a bar tender


from gettext import translation


print('Welcome to the tip calculator.\n')

total_bill = input('What was the total bill? ')
total_bill = total_bill.translate(total_bill.maketrans('$',' '))
total_bill = float(total_bill)

tip_percent = input('What tip would you like to give? 10, 12, or 15? ')
tip_percent = int(tip_percent)

tip_percent = tip_percent / 100
final_bill = total_bill + (total_bill * tip_percent)

bill_split = input('How many people to split the bill? ')
bill_split = int(bill_split)

pay_per_head = final_bill / bill_split

split_payment = round(pay_per_head, 2)

print(f'Each person should pay: ${split_payment} since it is ${pay_per_head} ')

