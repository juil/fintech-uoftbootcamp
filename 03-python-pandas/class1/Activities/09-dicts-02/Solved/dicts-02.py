# Use the `from` keyword to import the `shows` dictionary from the `show_data.py` file
from show_data import shows

# QUESTION 1: Who is the actor that plays Squidward in Spongebob (kids)?
print(shows['genre']['kids']['Spongebob']['cast'][3]['actor'])

# QUESTION 2: Patrick Warburton plays Joe Swanson in Family Guy (comedy). What is the link to his imdb page?
print(shows['genre']['comedy']['family_guy']['cast'][4]['imdb'])

# QUESTION 3: Is the Walking Dead still running?
print(shows['genre']['drama']['the_walking_dead']['still_running'])

# QUESTION 4: Who plays Dexter in Dexter (drama) and who plays Dexter in Dexter's Lab (kids)?
# HINT: You can print multiple items at once by using a comma like this: print(thing1, thing2)
print(shows['genre']['drama']['dexter']['cast'][0]['actor'], shows['genre']['kids']['dexters_lab']['cast'][0]['actor'])

# QUESTION 5: Who are the creators of Stranger Things (drama)?
print(shows['genre']['drama']['stranger_things']['creators'])

# QUESTION 6: Who hosts the Daily Show (talk)?
print(shows['genre']['talk']['the_daily_show']['host'])

# QUESTION 7: Who are all the hosts of the view (talk)
# Hint: You will need to use a loop for this one. You may not simply log the entire list, but must log each name individually
for person in shows['genre']['talk']['the_view']['host']:
    print(person)

# QUESTION 8: What are the show names of the Impractical Jokers (comedy)
# Hint: You will need to use a loop for this one. You may not simply log the entire list, but must log each name individually
for character in shows['genre']['comedy']['impractical_jokers']['cast']:
    print(character['showName'])

# QUESTION 9: Who does Will Arnett play in Arrested Development (comedy)
print(shows['genre']['comedy']['arrested_development']['cast'][2]['character'])

# QUESTION 10: Who plays Yami Yugi in Yu-Gi-Oh (kids)?
print(shows['genre']['kids']['yu_gi_oh']['cast'][0]['actor'])

# QUESTION 11: How many seasons did the Office (comedy) run?
print(shows['genre']['comedy']['the_office']['num_seasons'])

# QUESTION 12: Who are the main characters of the Office (comedy) (not the actors, but the actual character names)?
for character in shows['genre']['comedy']['the_office']['cast']:
    print(character['character'])

# QUESTION 13: List the characters in Teen Titans (kids)
for character in shows['genre']['kids']['teen_titans']['cast']:
    print(character['character'])

# QUESTION 14: What is the link to the IMDB page for the actor who plays Mr. Krabs (Spongebob, kids)?
print(shows['genre']['kids']['Spongebob']['cast'][1]['imdb'])

# QUESTION 15: Who plays Negan in The Walking Dead?
print(shows['genre']['drama']['the_walking_dead']['cast'][2]['actor'])

# QUESTION 16: List the main cast of Dexter (drama) (the actors, not the characters)
for character in shows['genre']['drama']['dexter']['cast']:
    print(character['actor'])

# QUESTION 17: Is Game of Thrones(drama) still running?
print(shows['genre']['drama']['game_of_thrones']['still_running'])

# QUESTION 18: Who does Peter Dinklage play in Game of Thrones (drama)?
print(shows['genre']['drama']['game_of_thrones']['cast'][1]['character'])

# QUESTION 19: List the American Idol Judges
for judge in shows['genre']['reality']['american_idol']['judges']:
    print(judge)

# QUESTION 20: Who plays Dustin in Stanger Things (drama)?
print(shows['genre']['drama']['stranger_things']['cast'][3]['actor'])
