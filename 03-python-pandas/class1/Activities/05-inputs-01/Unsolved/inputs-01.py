# Declare a variable `welcome_name` as an input with a string of "Welcome to the sandwich shop, what do I call you? ".
print('Welcome to the sandwich shop, what do I call you?')
name = input()

# Then print the string "Hello" concatenated with the variable `welcome_name`.
print(f'Hello {name}!')

# Declare a variable `question_sandwich` as an input with a string of "Are you here for a sandwich? (Yes or No?) ".
q_sandwich = input('Are you here for a sandwich? (Yes or No?) ')

# If `question_sandwich` is equal to true declare a variable `food_prompt` as an input with a string of "What kind of sandwich would you like?".
if q_sandwich == 'Yes':
    sandwichtype = input('What kind do you want? ')
# Then print a string of "Please wait 10 min for your " concatenated with the variable `food_prompt`.
    print(f'Please wait 10 min for you {sandwichtype}')
# Else If `question_sandwich` is false, print a string of "If you don't want a sandwich what are you here for?!".
elif q_sandwich == 'No':
    print('Then why are you here?')
# Else print a string of "You did not write Yes or No!"
else:
    print("That's not an option.")
