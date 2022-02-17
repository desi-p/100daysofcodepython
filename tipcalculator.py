#If the bill was $150.00, split between 5 people, with 12% tip
print("Welcome to the tip calculator!")
bill_amount = float(input("What is the amount of the total bill? "))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
tip_amount = float(input("How much of a tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
#Format the result to 2 decimal places = 33.60
result = float(bill_amount * (1 + tip_amount/100))/people

print("{:.2f}".format(result))