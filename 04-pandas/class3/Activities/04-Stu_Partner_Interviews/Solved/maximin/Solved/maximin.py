def maximin(numbers):

    # Initialize min and max number variables
    min_num = 0
    max_num = 0

    # Loop through each number in the list
    for number in numbers:

        # Check to see if min and max number variables are still initialized as 0
        # If so, set the min and max number variables to the first number
        # Else if the number is less than the min number, set the current number as the min number
        # Else if the number is greater than the max number, set the current number as the max number
        if min_num == 0 and max_num == 0:
            min_num = number
            max_num = number
        elif number < min_num:
            min_num = number
        elif number > max_num:
            max_num = number

    # Print the min and max numbers
    print(f"The minimum is {min_num} and the maximum is {max_num}")

# List of numbers
num_list = [12, 33, 41, 2, 61, 32, 75, 43, 67]

# Call the function
maximin(num_list)
