# Modules
import os
from pathlib import Path
import csv
import pandas as pd

# Prompt user for video lookup
lookup = input("Search Netflix: ")

# Set path for CSV file
path = "../Resources/netflix_ratings.csv"

# Open the file and loop through to search for the video
# netflixfile = os.open(path,os.O_RDONLY)
# If video is found, print title, rating, and user ratings. 
# If the video is never found, alert the user

csvreader = csv.reader(path,delimiter=',')

with open(path,'r') as netflix:
    fields = next(netflix).split(', ')
    print(fields)
    movie = False
    for i in netflix:
        if lookup.lower() in i.split(', ')[0].lower():
            print(i)
            movie = True
    if not movie:
        print(f"{lookup} not found.")

# os.close(netflixfile)
dataframe = pd.read_csv(path)
print(dataframe)
