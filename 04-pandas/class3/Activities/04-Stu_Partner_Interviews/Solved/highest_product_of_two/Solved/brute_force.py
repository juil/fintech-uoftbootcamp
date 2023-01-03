def max_product_of_two(list_param):
    # Initialize max_product variable
    max_product = 0

    # Loop through the numbers in the list
    for num_one in list_param:
        # Print the num_one
        print(num_one)

        # Loop through the numbers in the list again
        for num_two in list_param:

            # Check to make sure the same number is not being multiplied
            if num_one != num_two:

                # If so, calculate the current product
                current_product = num_two * num_one

                # If the max_product is equal to 0, set the max_product to the current_product
                # Else if the max_product is less than the current_product, set the max_product to the current_product
                if max_product == 0:
                    max_product = current_product
                elif max_product < current_product:
                    max_product = current_product

                # Print the num_two, current_product, and max_product variables
                print(f"   {num_two} : {current_product} : {max_product}")

    return max_product

# List of numbers
list_nums = [-100, 2, 42, 100]

# Call the function
highest_product = max_product_of_two(list_nums)

# Print the highest product
print(f"The highest product is {highest_product}.")
