# -*- coding: utf-8 -*-
"""Student Do: Sales Analysis.

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, and iterate over each
row of the file to calculate customer sales averages.
"""

# @TODO: Import the pathlib and csv library
from pathlib import Path
import csv


# @TODO: Set the file path
filepath = Path().absolute() / 'resources/sales.csv'
print(filepath)
print(f'Exists? {filepath.exists()}')

# @TODO: Initialize dictionary
analysis = {}

# @TODO: Open the csv file as an object
with open(filepath, 'r') as sales:
    # @TODO:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(sales,delimiter=',')

    # @TODO: Read the header row first (skip this step if there is no header)
    header = next(csvreader)

    # @TODO: Print the header
    print(f'Header: {header}')

    # @TODO: Read each row of data after the header
    for i in csvreader:
        # @TODO: Print the row
        # print(f'{i}')
        # @TODO:
        # Set the 'name', 'count', and 'revenue' variables for better
        # readability, convert strings to ints for numerical calculations
        name = i[0]
        count = int(i[1])
        revenue = int(i[2])

        # @TODO: Calculate the average and round to the nearest 2 decimal places
        average = round(revenue/count, 2)
        # @TODO:
        # If name is not already in the analysis dict, initialize the dictionary
        # Else continue to add to the existing key and nested key-value pairs
        if analysis.get(name) == None:
            analysis.update({name:  
                           {'count': count, 'revenue': revenue, 
                            'average': average}})
            print(f'Add {name}: {analysis[name]}')
        else:
            analysis[name]['count'] += count
            analysis[name]['revenue'] += revenue
            analysis[name]['average'] = round(analysis[name]['revenue'] / analysis[name]['count'], 2)
            print(f'Update {name}: {analysis[name]}')


# @TODO: Set the header for aggregate.csv
header = ['name', 'count', 'revenue', 'average']

# @TODO: Set the path for the aggregate.csv
outputpath = Path().absolute() / 'resources/aggregate.csv'
# @TODO:
# Open the output path as a file and pass into the 'csv.writer()' function
# Set the delimiter/separater as a ','
with open(outputpath, 'w') as csvfile:
    # csvwriter = csv.DictWriter(csvfile,fieldnames=header)
    csvwriter = csv.writer(csvfile,delimiter=',')

    # @TODO: Write the header as the first row
    # csvwriter.writeheader()
    csvwriter.writerow(header)
    # @TODO:
    # Loop over every key in analysis and write the associated key (name) and
    # nested key-value pairs (metrics)
    # csvwriter.writerows(analysis)
    for key in analysis: 
        rep = analysis[key]
        csvwriter.writerow([key,rep['count'],rep['revenue'],rep['average']])
