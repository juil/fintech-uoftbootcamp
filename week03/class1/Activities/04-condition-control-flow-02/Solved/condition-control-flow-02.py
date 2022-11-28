
######################
# Create Character One
######################

# Make a variable called `c1_name` and have it equal a string of "Mr. Farley".
c1_name = "Mr. Farley"

# Make a variable called `c1_age` and have it equal to an integer of 65.
c1_age = 65

# Make a variable called `c1_profession` and have it equal to "Web Developer".
c1_profession = "Web Developer"

# Make a variable called `c1_salary` and have it equal to 100000.
c1_salary = 100000

# Make a variable called `c1_species` and have it equal to "cat".
c1_species = "cat"

# Make a variable called `c1_location` and have it equal to "San Francisco, CA".
c1_location = "San Francisco, CA"

# Make a variable called `c1_monthly_rent` and have it equal to 2000.
c1_monthly_rent = 2000

# Make a variable called `c1_monthly_expenses` and have it equal to 1500.
c1_monthly_expenses = 1500

# Make a variable called `c1_yearly_rent` and have it equal to `c1_monthly_rent` * 12.
c1_yearly_rent = c1_monthly_rent * 12

# Make a variable called `c1_yearly_expenses` and have it equal to 1500.00 * 12
c1_yearly_expenses = c1_monthly_expenses * 12

# Make a variable called `c1_savings` and have it equal to `c1_salary` - (`c1_yearly_rent` + `c1_yearly_expenses`)
c1_savings = c1_salary - (c1_yearly_rent + c1_yearly_expenses)


######################
# Create Character Two
######################

# Make a variable called `c2_name` and have it equal a string of "Mr. Snuggles".
c2_name = "Mr. Snuggles"

# Make a variable called `c2_age` and have it equal to an integer of 30.
c2_age = 30

# Make a variable called `c2_species` and have it equal to "mouse".
c2_species = "mouse"

# Make a variable called `c2_profession` and have it equal "Accountant"
c2_profession = "Accountant"

# Make a variable called `c2_salary` and have it equal to 70000.
c2_salary = 70000

# Make a variable called `c2_location` and have it equal to "Oakland, CA".
c2_location = "Oakland, CA"

# Make a variable called `c2_monthly_rent` and have it equal to 4000.
c2_monthly_rent = 4000

# Make a variable called `c2_monthly_expenses` and have it equal to 500.
c2_monthly_expenses = 500

# Make a variable called `c2_yearly_rent` and have it equal to `c2_monthly_rent` * 12.
c2_yearly_rent = c2_monthly_rent * 12

# Make a variable called `c2_yearly_expenses` and have it equal to `c2_monthly_expenses` * 12.
c2_yearly_expenses = c2_monthly_expenses * 12

# Make a variable called `c2_savings` and have it equal to `c2_salary` - (`c2_yearly_rent` + `c2_yearly_expenses`)
c2_savings = c2_salary - (c2_yearly_rent + c2_yearly_expenses)

##############
# Conditionals
##############

# Write an if-else statement to check if `c1_name` is equal to "Mr. Farley". If so, print a string of "Hello Mr. Farley" using the `c1_name` variable. If not, print a string of "Hello stranger".
if c1_name == "Mr. Farley":
    print(f"Hello {c1_name}.")
else:
    print("Hello stranger!")

# Write an if-else statement to check if `c2_age` is greater than `c1_age`. If so, print a string of "Mr. Farley is older than Mr. Snuggles". Else if `c1_age` is greater than `c2_age`, print a string of "Mr. Snuggles is older than Mr. Farley". Else, `c1_age` must be equal to `c2_age`, therefore print a string of "Mr. Farley is the same age as Mr. Snuggles".
if c2_age > c1_age:
    print("Mr. Farley is older than Mr. Snuggles.")
elif c1_age > c2_age:
    print("Mr. Snuggles is older than Mr. Farley.")
else:
    print("Mr. Farley is the same age as Mr. Snuggles.")

# Write an if-else statement to check if `c1_location` is equal to "Oakland, CA". If so, print a string of "Mr. Farley comes from the home of the Raiders!". Else if `c2_location` is equal to a string of "San Francisco, CA", print a string of "Mr. Farley comes from the home of the 49ers!". Else both conditions must not apply and therefore print a string "Mr. Farley doesn't hail from a sports town."
if c1_location == "Oakland, CA":
    print("Mr. Farley comes from the home of the Raiders!")
elif c1_location == "San Francisco, CA":
    print("Mr. Farley comes from the home of the 49ers!")
else:
    print("Mr. Farley doesn't hail from a sports town.")

# Write an if-else statement to check if `c1_rent` is greater than `c2_rent`. If so, print a string of "Mr. Farley pays more rent than Mr. Snuggles". Else if `c1_rent` is less than `c2_rent`, print a string of "Mr. Farley pays less rent than Mr. Snuggles". Else, `c1_rent` must be equal to `c2_rent`, therefore print a string of "Mr. Farley pays the same rent as Mr. Snuggles".
if c1_yearly_rent > c2_yearly_rent:
    print("Mr. Farley pays more rent than Mr. Snuggles.")
elif c1_yearly_rent < c2_yearly_rent:
    print("Mr. Farley pays less rent than Mr. Snuggles.")
else:
    print("Mr. Farley pays the same rent as Mr. Snuggles.")

# Write an if-else statement to check if `c1_monthly_expenses` is greater than `c2_monthly_expenses`. If so, print a string of `Mr. Farley has more expenses than Mr. Snuggles`. Else if `c1_monthly_expenses` is less than `c2_monthly_expenses`, print a string of "Mr. Farley pays less expenses than Mr. Snuggles". Else, `c1_monthly_expenses` must be equal to `c2_monthly_expenses`, therefore print a string of "Mr. Farley pays the same expenses as Mr. Snuggles".
if c1_yearly_expenses > c2_yearly_expenses:
    print("Mr. Farley has more expenses than Mr. Snuggles.")
elif c1_yearly_expenses < c2_yearly_expenses:
    print("Mr. Farley pays less expenses than Mr. Snuggles.")
else:
    print("Mr. Farley pays the same expenses as Mr. Snuggles.")

# Write an if-else statement to check if `c1_profession` is equal to "Web Developer" AND `c2_profession` is equal to "Accountant". If so, print a string of "They are a Web Developer and an Accountant", else print a string of "They are professionals."
if c1_profession == "Web Developer" and c2_profession == "Accountant":
    print("They are a Web Developer and an Accountant.")
else:
    print("They are professionals.")
