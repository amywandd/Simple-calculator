#Amy Njeri Wanderi - sct211-0010/2021
bill = int(input("What is the bill amount?"))
#calculates tip amount
tip = int(input("What is the tip amount: 10,12 or 15?"))
if tip not in [10, 12, 15]:
    print("Not acceptable")
elif tip == 10:
    tip2 = 10 * tip
    tip_amount = tip2 / 100
elif tip == 12:
    tip2 = 12 * tip
    tip_amount = tip2 / 100
elif tip == 15:
    tip2 = 15 * tip
    tip_amount = tip2 / 100
people = int(input("How many people are splitting the bill?"))
#calculate total bill
total_bill = bill + tip_amount
#calculate how much each person should pay
divided_cost = total_bill / people
print("Each person should pay {:2f}".format(divided_cost))
