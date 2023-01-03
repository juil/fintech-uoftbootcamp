# Declare a variable `welcome_name` as an input with a string of "Welcome to the sandwich shop, what do I call you?".
welcome_name = input("Welcome to the sandwich shop, what do I call you? ")

# Then print the string "Hello" concatenated with the variable `welcome_name`.
print(f"Hello {welcome_name}")

# Declare a variable `question_sandwich` as an input with a string of "Are you here for a sandwich?".
question_sandwich = input("Are you here for a sandwich? Yes or No?")

# If `question_sandwich` is equal to true declare a variable `food_prompt` as an input with a string of "What kind of sandwich would you like?".
# Then print a string of "Please wait 10 min for your " concatenated with the variable `food_prompt`.
# Else If `question_sandwich` is false, print a string of "If you don't want a sandwich what are you here for?!".
# Else print a string of "You did not write Yes or No!"
if question_sandwich == "Yes":
    food_prompt = input("What kind of sandwich would you like?")
    print(f"Please wait 10 mins for your {food_prompt}")
elif question_sandwich == "No":
    print("If you don't want a sandwich what are you here for?!")
else:
    print("You did not write Yes or No!")
