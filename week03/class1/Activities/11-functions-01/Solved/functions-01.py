# Define a function `having_fun` that prints "Functions are FUN!".
def having_fun():
    print("Functions are FUN!")

# Define a function `thirty_seven` that prints the sum of 18 and 19.
def thirty_seven():
    sum = 18 + 19
    print(sum)

# Call the two functions you've defined so far.
having_fun()
thirty_seven()

# Define a function `hello` that takes in a string parameter and prints the parameter variable.
def hello(string_param):
    print(string_param)

# Call your `hello` function.
hello("Hello World!")

# Define a function `user_input` that asks the user "What is your name?" and stores it in a variable called `user_name` and print the user's name.
def user_input():
    user_name = input("What is your name? ")
    print(user_name)

# Call your `user_input` function.
user_input()

# Define a function `good_day` that creates an input dialogue asking the user "Are you having a nice day?" and prints the response.
def good_day():
    response = input("Are you having a nice day? ")
    print(response)

# Call your `good_day` function.
good_day()

# Define a function `average` that calculates the average between two parameters and returns the average.
def average(num_1, num_2):
    avg_calc = num_1 + num_2 / 2
    return avg_calc

# Call the `average` function and assign it to a variable `calculated_average`.
calculated_average = average(90, 10)
print(f"Calculated Average: {calculated_average}")
