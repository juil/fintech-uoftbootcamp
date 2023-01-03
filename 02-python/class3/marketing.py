# -*- coding: utf-8 -*-
"""Refresher activity.

This script will use variables, conditionals, lists, dicts, and functions
to print out different greetings for customers based on their
business tier (determined by revenue).
"""

# List of dicts
customers = [
    { "first_name": "Tom", "last_name": "Bell", "revenue": 0 },
    { "first_name": "Maggie", "last_name": "Johnson", "revenue": 1032 },
    { "first_name": "John", "last_name": "Spectre", "revenue": 2543 },
    { "first_name": "Susy", "last_name": "Simmons", "revenue": 5322 }
]

# @TODO Define a function that accepts a customer first_name, last_name, and
# revenue and returns a custom greeting with the full name.
# Use these ranges to determine the business tier (and corresponding message)
# for each customer.
#   Platinum = 3001+
#   Gold = 2001-3000
#   Silver = 1001-2000
#   Bronze = 0-1000
def create_greeting(first_name, last_name, revenue):
    # @TODO: YOUR CODE HERE!
    greeting = "Welcome " + first_name + " " + last_name + ".\n"
    if revenue > 3000:
        greeting += "Our most valued Platinum customer!"
    elif revenue > 2000:
        greeting += "Our valued Gold customer!"
    elif revenue > 1000:
        greeting += "Our Silver customer."
    else:
        greeting += "..."
    return greeting

# customer is dict entry
def print_greeting(customer):
    print(f"{create_greeting(customer['first_name'], customer['last_name'], customer['revenue'])}")
    return

for i in range(len(customers)):
    print_greeting(customers[i])

# @TODO: Loop through the list of customers and use your function to print
# custom greetings for each customer.
# @TODO: YOUR CODE HERE!
