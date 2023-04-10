# Ask the user for their gross income and number of dependents
gross_income = float(input("Enter your gross income to the nearest penny: "))
num_dependents = int(input("Enter the number of dependents you have: "))

# Calculate the taxable income
standard_deduction = 10000
dependent_deduction = 3000
taxable_income = gross_income - standard_deduction - (dependent_deduction * num_dependents)

# Calculate the tax
tax_rate = 0.2
tax = taxable_income * tax_rate

# Print the result
print("Your taxable income is:", taxable_income)
print("Your income tax is:", tax)