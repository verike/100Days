# This calculator is used to calculate the percentage tip given to a person probably a bar tender


from gettext import translation


print('Welcome to the tip calculator.\n')

total_bill = input('What was the total bill? ')
total_bill = total_bill.translate(total_bill.maketrans('$',' '))
total_bill = float(total_bill)

tip_percent = int(input('What tip would you like to give? 10, 12, or 15? '))

tip_percent = tip_percent / 100
# final_bill = total_bill + (total_bill * tip_percent)  #Conventional way of calculating the added percentage of a number

final_bill = total_bill * (1.0 + tip_percent)
# A shortcut to add the percentage of the bill to the original bill

bill_split = input('How many people to split the bill? ')
bill_split = int(bill_split)

pay_per_head = final_bill / bill_split

split_payment = round(pay_per_head, 2)
final_payment = '{:.2f}'.format(pay_per_head)
# Use The round function to round the result to two (2) decimal places
# The round up formatting '{:.2f}'.format(pay_per_head) is strictly to round the result up to two decimal places.

print(f'Each person should pay: ${final_payment} since it is ${pay_per_head} ')