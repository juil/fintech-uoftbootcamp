# -*- coding: utf-8 -*-
"""
Student Do: Trading Log.

This script demonstrates how to perform basic analysis of trading profits/losses
over the course of a month (20 business days).
"""

# @TODO: Initialize the metric variables

total = 0
count = 0
maximum = 0
minimum = 0


# @TODO: Initialize lists to hold profitable and unprofitable day profits/losses

profitable_days = []
unprofitable_days = [] 


# List of trading profits/losses
trading_pnl = [ -224,  352, 252, 354, -544,
                -650,   56, 123, -43,  254,
                 325, -123,  47, 321,  123,
                 133, -151, 613, 232, -311 ]

# @TODO: Iterate over each element of the list

for i in range(len(trading_pnl)):
    # @TODO: Cumulatively sum up the total and count
    total += trading_pnl[i]
    count += 1

    # @TODO: Write logic to determine minimum and maximum values
    if trading_pnl[i] < minimum:
        minimum = trading_pnl[i]
    elif trading_pnl[i] > maximum:
        maximum = trading_pnl[i]

    # @TODO: Write logic to determine profitable vs. unprofitable days
    if trading_pnl[i] > 0:
        profitable_days.append(trading_pnl[i]) 
    elif trading_pnl[i] < 0:
        unprofitable_days.append(trading_pnl[i])

# @TODO: Calculate the average
total_pnl = sum(trading_pnl)
average = total_pnl/len(trading_pnl)
print(f'Average PNL: ${average:.2f}')

# @TODO: Calculate count metrics
print('**Summary Statistics**')

# @TODO: Calculate percentage metrics



# @TODO: Print out the summary statistics

