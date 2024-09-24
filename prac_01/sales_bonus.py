"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    if sales < 1000:
        bonus = 0.1
    else:
        bonus = 0.15
    print bonus
    get sales
display invalid input
"""
MINIMAL_SALES = 0
REQUIRED_SALES = 1000
MINIMAL_BONUS = 0.1
MAXIMUM_BONUS = 0.15
sales = float(input("Enter sales: $"))
while sales >= MINIMAL_SALES:
    if sales < REQUIRED_SALES:
        bonus = MINIMAL_BONUS
    else:
        bonus = MAXIMUM_BONUS
    print(f"Your bonus is {bonus}% which gives you a total outcome of ${sales * bonus}")
    sales = float(input("Enter sales: $"))
print("Invalid input")
