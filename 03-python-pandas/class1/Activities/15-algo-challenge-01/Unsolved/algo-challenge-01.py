# Import the `random` library.
import random

# Answer each question with the correct coding solution.

# QUESTION 1: Create a function called `number_guess` that takes in an integer as an argument.
# If the number is 42, print(true). If it isn't 42, print(false)

# YOUR CODE HERE
def number_guess(num):
    print(int(num) == 42)

number_guess(input("Guess: "))

# QUESTION 2: Write a function that takes in a list of numbers. the function should print the smallest number in the given list

# YOUR CODE HERE
def smallest(numlist):
    print(min(numlist))

smallest([1,2,3,4])

# QUESTION 3: Write a function which takes in a list of strings. The function should print the shortest string in the list.

# YOUR CODE HERE


#QUESTION 4: Write a function that takes in three arguments: a high value, a low value and a list of numbers.
# The function should print a new list of numbers where the elements are greater than the low value and less than the high value

# YOUR CODE HERE
def between(high, low, numlist):
    newlist = []
    for i in numlist:
        if low < i and i < high:
            newlist.append(i)
    print(newlist)

nums = [1,2,3,4,5,6,6,7,8]
between(5,2,nums)
