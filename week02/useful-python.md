# Useful Python

## Resources

### Courses

- freeCodeCamp.org - [Python beginner course (4.5hr)](https://www.youtube.com/watch?v=rfscVS0vtbw)
- https://www.youtube.com/@freecodecamp - a YouTube channel with thousands of hours of free programming tutorials
- https://www.edx.org/course/introduction-computer-science-harvardx-cs50x - Harvard University's intro to Computer Science (also free)
- https://ocw.mit.edu/search/?d=Electrical%20Engineering%20and%20Computer%20Science&f=Lecture%20Videos&q=computer - Free access to MIT lectures, highly informational
- Recommended by Jonathan Coleman


### Books

Python Crash Course - Eric Matthes [[Amazon](https://www.amazon.ca/Python-Crash-Course-Eric-Matthes/dp/1593279280)]

## Commands

### Output commas and set number of decimal points

	print(f'Number: {var:,.2f}')

	return('{:,}'.format(number))

[PythonGuides](https://pythonguides.com/python-format-number-with-commas/)

## Libraries

NumPy-Financial
	import numpy_financial as np

PathLib
	from pathlib import Path

CSV
```
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)
```
https://www.geeksforgeeks.org/writing-csv-files-in-python/

## Iterate through dictionary

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

## Math

Rounding

```
round(myFloat, 2)
format(myFloat, '.2f')
```
https://tutorialdeep.com/knowhow/round-float-to-2-decimal-places-python/
