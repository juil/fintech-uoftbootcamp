# Useful Python

## Resources

### Courses

freeCodeCamp.org - [Python beginner course (4.5hr)](https://www.youtube.com/watch?v=rfscVS0vtbw)

### Books

Python Crash Course - Eric Matthes [[Amazon](https://www.amazon.ca/Python-Crash-Course-Eric-Matthes/dp/1593279280)]

## Commands

### Output commas and set number of decimal points

	print(f'Number: {var:,.2f}')

	return('{:,}'.format(number))

[PythonGuides](https://pythonguides.com/python-format-number-with-commas/)

### Iterate through dictionary

```
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> for key in a_dict:
...     print(key, '->', a_dict[key])
...
```
color -> blue
fruit -> apple
pet -> dog

[More Info](https://realpython.com/iterate-through-dictionary-python/)
