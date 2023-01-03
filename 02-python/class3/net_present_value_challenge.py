# -*- coding: utf-8 -*-
"""Student Activity: Financial Analysis using NPV.

This script will choose the optimal project scenario to
undertake based on max NPV values.
"""

# @TODO: Import the NumPy Financial (numpy_financial) library
import numpy_financial as np

# Discount Rate
discount_rate = .1

# Initial Investment, Cash Flow 1, Cash Flow 2, Cash Flow 3, Cash Flow 4
cash_flows_conservative = [-1000, 400, 400, 400, 400]
cash_flows_neutral = [-1500, 600, 600, 600, 600]
cash_flows_aggressive = [-2250, 800, 800, 800, 800]

# @TODO: Initialize dictionary to hold NPV return values
npv_dict = {'conservative':0,
            'neutral':0,
            'aggressive':0}

# @TODO: Calculate the NPV for each scenario

npv_dict['conservative'] = np.npv(discount_rate,cash_flows_conservative)
npv_dict['neutral'] = np.npv(discount_rate,cash_flows_neutral)
npv_dict['aggressive'] = np.npv(discount_rate,cash_flows_aggressive)

print(f'Net Present Value: {npv_dict}')
print(f'Max NPV: {max(npv_dict)} = {npv_dict[max(npv_dict)]:.2f}')

# @TODO: Initialize variables



# @TODO: Iterate over npv_dict to find the max key-value pair










# @TODO: Print out the optimal project scenario with the highest NPV value
