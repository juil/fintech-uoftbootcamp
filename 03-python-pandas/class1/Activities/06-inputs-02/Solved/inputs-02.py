# Declare a variable of `name` with an input and a string of "Welcome to the Boba Shop! What is your name?".
name = input("Welcome to the Boba Shop! What is your name?")

# Check if `name` is not an empty string or equal to `None`.
if name != "" or name == None:
    # If so, write a print statement with a string of "Hello" concatenated with the variable `name`.
    print(f"Hello {name}")

    # Then, declare a variable of `beverage` with an input and a string of "What kind of boba drink would you like?".
    beverage = input("What kind of boba drink would you like?")

    # Then, Declare a variable of `sweetness` with an input and a string of "How sweet do you want your drink: 0, 50, 100, or 200?".
    sweetness_level = int(input("How sweet do you want your drink: 0, 50, 100, or 200?"))

    # If `sweetness` equals 50 print "half sweetened".
    if sweetness_level == 50:
        sweetness = "half sweetened"
    # Else if `sweetness` 100 print "normal sweet".
    elif sweetness_level == 100:
        sweetness = "normal sweet"
    # Else if `sweetness` 200 print "super sweet".
    elif sweetness_level == 200:
        sweetness = "super sweet"
    # Else print with a string of "non-sweet".
    else:
        sweetness = "non-sweet"

    # Then print the string of "Your order of " concatenated with the variable `beverage`, concatenated with " boba with a sweet level of ", concatenated with the variable `sweetness`
    print(f"Your order of {beverage} boba with a sweetness level of {sweetness}")

# Else, print the string of "You didn't give us your name! Goodbye".
else:
    print("You didn't give us your name! Goodbye")

