# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Mike
organize his grocery shopping list.
"""

# @TODO: Create a list of groceries

groceries = ['water', 'butter', 'eggs', 'apples', 'cinnamon', 'sugar', 'milk']

# @TODO: Find the first two items on the list

print(f'First two grocery items: {groceries[:2]}')

# @TODO: Find the last five items on the list

print(f'Last 5: {groceries[-5:]}')

# @TODO: Find every other item on the list, starting from the second item

print(f'Every other item: {groceries[1::2]}')

# @TODO: Add an element to the end of the list

new = 'bread'
groceries.append(new)
print(f'Add {new}: {groceries}')

# @TODO: Changes a specified element within the list at the given index

i = 2
new2 = 'cheese'
print(f'Change item #{i+1}: {groceries[i]}')
# groceries.pop(i)
# groceries.insert(i, new2)
groceries[i] = new2
print(f'{groceries}')

# @TODO: Calculate how many items you have in the list

print(f'Your grocery list has {len(groceries)} items.')
