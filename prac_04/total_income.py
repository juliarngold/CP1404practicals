"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    total_number_of_months = int(input(f"How many months? "))

    for month in range(1, total_number_of_months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes, total_number_of_months)


def print_report(incomes, total_number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_number_of_months + 1):
        income, total = calculate_income(incomes, total, month)
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def calculate_income(incomes, total, month):
    income = incomes[month - 1]
    total += income
    return income, total


main()
