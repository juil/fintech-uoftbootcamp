# Import the `string` library.
import string

# Use the `string` library to initialize string variables representing all valid letters and digits, respectively.
validletters = string.ascii_letters
validdigits = string.digits

# Define a function called `check_strength` that takes in a string parameter called `password`.
def check_strength(password):
    # Create two boolean variables called `contains_number` and `contains_letter`. Set them to False.
    contains_number = False
    contains_letter = False

    # Initialize a `count` variable and set it to 0.
    count = 0

    # Loop through each character in the `password` and increment the `count` variable by 1 for each character.
    for i in list(password):
        count += 1

        # Create an if-else statement that loops through each character in `password` and updates `contains_number` or `contains_letter` to True.
        if i in validletters:
            contains_letter = True
        if i in validdigits:
            contains_number = True

    # If `password` contains equal to or fewer than 6 characters and consists only of numbers, print "Your password is too weak."
    # Else if `password` contains more than 6 characters and consists of at least one number and at least one letter, print "Your password is a strong password".
    # Else, print "Your password is of average strength."
    if count <= 6 and not contains_letter:
        print("Your password is too weak.")
    elif count > 6 and contains_letter and contains_number:
        print("Your password is a strong password")
    else:
        print("Your password is of average strenght.")

check_strength(input("New Password: "))

# Declare a variable as `user_input_password` with an input stating "Input your password: ".


# Call the check_strength function with the `user_input_password`.
