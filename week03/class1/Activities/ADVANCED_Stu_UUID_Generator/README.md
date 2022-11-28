# UUID String Generator

In this activity, you will generate a universally unique ID (UUID) string using functions and module imports.

## Instructions

1. Import the [random](https://docs.python.org/3/library/random.html) and [string](https://docs.python.org/3/library/string.html) modules.

2. Create a function that returns a universally unique ID (UUID).

    * The function should accept a parameter for UUID length with the default size of 4.

    * The function should accept a parameter for a string of characters.

    * This string of characters will be the alphabet used to generate the UUID.

    * For example, if we pass `'abcdef'`, the UUID can only consist of the letters 'abcdef'.

    * The length and characters parameters should be optional and have default values.

3. Define a default character alphabet using the constants provided by the [string module](https://docs.python.org/3/library/string.html).

4. To select random characters from the alphabet for your UUID, use one of the functions available for sequence selection in the [random module](https://docs.python.org/3/library/random.html).

5. Complete the test function to generate a variety of UUIDs and print them to the console.

## Hints

* Define a default character alphabet that combines ASCII letters with digits.

* The random module has a function for making a random choice from an array. See the documentation for [functions for sequences](https://docs.python.org/3/library/random.html#functions-for-sequences).

* The code for the UUID function should create a list, append `length` random characters to the list, and then return the result of using `join` to create a string from the list.

* See [Stack Overflow](https://stackoverflow.com/questions/292965/what-is-a-uuid) for more info on UUIDs.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
