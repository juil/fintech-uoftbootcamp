def pig(string):
    # Use built-in method to delete common punctuation marks
    strip_commas = string.replace(",", "")
    strip_period = strip_commas.replace(".", "")
    strip_semi_colon = strip_period.replace(";", "")

    # Transform string into a list for word manipulation
    word_list = strip_semi_colon.split(" ")

    # An empty list that will hold pig latinized words
    piggified_list = []

    # Iterate through each word to pig latinize it
    for word in word_list:
        # Add the first letter to the end, then add 'ay'
        pig_word = word[1:] + word[0] + 'ay'
        piggified_list.append(pig_word)

        # Transform list back into a string
        pig_latinized_string = (' ').join(piggified_list)

    # Return the pig latin words
    return pig_latinized_string

# Call the function
pig_latin = pig("your car is very nice")

# Print the pig latinized words
print(pig_latin)
