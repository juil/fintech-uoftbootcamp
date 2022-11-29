# Import the necessary libraries for reading csv files
from pathlib import Path
import csv
import pandas

# Set the path for the csv file
filepath = Path().absolute() / '../Resources/pokemon.csv'

# Create new lists to store data for heaviest and tallest pokemon
heaviest = []
tallest = []

# Open the csv
with open(filepath, 'r') as pokemon:
    csvreader = csv.reader(pokemon,delimiter=',')
    # Iterate through the data and search for the number the user inputted. Remember to skip the header of the CSV.
    fields = next(pokemon)
    print(fields)
    # pokemon_num = input("Search Pokemon #: ")
    search = []
        # Print the name of the pokemon(identifier) and pokedex number(species id) at that number. For example, "Pokemon No. 25 - pikachu".
    dataframe = pandas.read_csv(filepath)
    # print(dataframe)
    
    pokemon_num = input("Search #: ")
    p = []
    for i in csvreader:
        if i[0] == pokemon_num: p = i
    print(f"Pokemon No. {pokemon_num} - {p[1]}")

        # Iterate through the data and search for pokemon whose weight is greater than 3000. Append only the pokemon's name and weight to the 'heaviest' list.


        # Iterate through the data and search for pokemon whose height is greater than 50. Append only the pokemon's name and height to the 'tallest' list.


# Print the list of heaviest and tallest pokemon

