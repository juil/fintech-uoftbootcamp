# @TODO: Your code here

# Import libraries
import csv
from pathlib import Path 

# Path to CSV file
file = Path().absolute() / "../Resources/employees.csv"
print(f'Exists? {Path(file).exists()}')

# Company URL for email
companyurl = 'spacex.com'

# Read CSV file as dict
with open(file, 'r') as employees:
    #print(employees[0])
    dictreader = csv.DictReader(employees,delimiter=',')
    print(dictreader)

    # List of employee dicts
    new_employee_data = []

    for row in dictreader:
        new_employee_data.append({'first_name': row.get('first_name'), 
                                  'last_name': row.get('last_name'), 
                                  'ssn': row.get('ssn'), 
                                  'email': row.get('first_name').lower() +
                                  '.' + row.get('last_name').lower() + 
                                  '@' + companyurl})
        print(f"Added: {new_employee_data[-1]}")

# Output list as new CSV file

