# Useful Python

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
