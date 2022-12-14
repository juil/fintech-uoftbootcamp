"""
Determine the Compound Annual Growth Rate for an investment
"""

# Declare a variable beginning_balance as a float
beginning_balance = 29000.00

# Declare a variable ending_balance as float
ending_balance = 45000.00

# Declare a variable years as a float
years = 1.0

# Define a function called calculate_compound_growth_rate with three arguments: beginning_balance, ending_balance, years. Function should output growth_rate.
def calculate_compound_growth_rate(beg_bal,end_bal,years):
    return ((end_bal/beg_bal)**(1/years))-1

def cagr(b, e, y):
    return calculate_compound_growth_rate(b,e,y)

# Call calculate_compound_growth_rate using beginning_balance, ending_balance, and years. Capture as year_one_growth.

# Initialize global variable annualgrowth

def print_growthrate(beg_bal,end_bal,year):
    print(f'Year {int(year)}:')
    annualgrowth = cagr(beg_bal,end_bal,year)*100
    print(f'Beginning Balance: ${beg_bal:,.2f}\n' +
          f'Ending Balance: ${end_bal:,.2f}\n' +
          f'Years: {year:.1f}\n' +
          f'CAGR: {annualgrowth:.2f}%')
    return annualgrowth

year1cagr = print_growthrate(beginning_balance,ending_balance,years)

# Update beginning_balance and ending balance for year two, and then execute calculate_compound_growth_rate
def newyear():
    beginning_balance = ending_balance
    # years += 1
    return


ending_balance = ending_balance * 1.69420

newyear()
year2cagr = print_growthrate(beginning_balance,ending_balance,years)


# Call calculate_compound_growth_rate using beginning_balance, ending_balance, and years. Capture as year_two_growth.


# Update beginning_balance and ending balance for year three, and then execute calculate_compound_growth_rate


# Call calculate_compound_growth_rate using beginning_balance, ending_balance, and years. Capture as year_three_growth.

# Use Python round() function to round year_one_growth, year_two_growth, and year_three_growth. Capture these as new variables.

# Print year_one_growth, year_two_growth, year_three_growth as percents using string formatting


# Challenge

# Create a global, empty list
growth_rates = []

# Define a function called


    # Populate growth_rates list using add() function


# Call calculate_compound_growth_rate_list and populate growth_rates with 2016 values (beginning_balance and ending_balance)
beginning_balance = 29000.00
ending_balance = 45000.00


# Call calculate_compound_growth_rate_list and populate growth_rates with 2017 values (beginning_balance and ending_balance)
beginning_balance = 45000.00
ending_balance = 47000.00


# Call calculate_compound_growth_rate_list and populate growth_rates with 2018 values (beginning_balance and ending_balance)
beginning_balance = 47000.00
ending_balance = 48930.00


# Print growth_rates list
print("Growth rates: ", growth_rates)
