"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


lower_than1000 = 0.1
higher_than1000 = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * lower_than1000
        print("Bonus: {:.2f}".format(bonus))
    elif sales >= 1000:
        bonus = sales * higher_than1000
        print("Bonus: {:.2f}".format(bonus))
    else:
        print("Invalid value")
    sales = float(input("Enter sales: $"))
