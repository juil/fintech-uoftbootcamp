# -*- coding: utf-8 -*-
"""Student Do: E-Commerce Traffic.

This script will parse through a text file and sum the total
number of customers and the count of days in the text file to
calculate the daily average of customer traffic for an e-commerce
business.
"""

# @TODO: From the pathlib library, import the main class Path

from pathlib import Path
import os

# @TODO: Check the current directory where the Python program is executing from
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = Path().absolute()
print(dir_path)

# @TODO: Set the path using Pathlib
customer_traffic_path = dir_path / 'resources/customer_traffic.txt'
print(customer_traffic_path)

# Initialize variables
customer_total = 0
day_count = 0

# @TODO: Open the file in "read" mode ('r') and store the contents in the variable 'file'
with open(customer_traffic_path, 'r') as file:
    # @TODO: Parse the file line by line
    for line in file:

        # @TODO: Convert the number in the text file from string to int (allows for numerical calculations)
        customer = int(line)
        
        # @TODO: Sum the total and count of the numbers in the text file
        customer_total += customer
        day_count += 1

# @TODO: Print out customer_total and day_count
print(f'{customer_total} customers over {day_count} days.')



# @TODO: Calculate the average



# @TODO: Set output file name


# @TODO: Open the output path as a file object

    # @TODO: Write daily_average to the output file, convert to string
