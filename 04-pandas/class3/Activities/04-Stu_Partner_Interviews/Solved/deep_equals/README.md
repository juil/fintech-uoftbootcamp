# Deep Equals

Suppose you have two lists with the same contents.

```python
list first = [1, 2, 3];
list second = [3, 2, 1];
```

Write a function that tests if the contents of two lists are equal.

## Notes to the Interviewer

If you compare the two lists using `==` then the result is false even though the contents of the lists are the same. This is because simple list equality also includes the order of elements:

[Python Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)
> "Sequences compare lexicographically using comparison of corresponding elements, whereby reflexivity of the elements is enforced."

```python
# Output: False
print(first == second)
```

If we want to compare the _contents_ of two lists, we have to write our own function to do so.

## Prompts from the Interviewer

* **Prompt**: Can you explain why `first == second` returns false?

  * **Look For:**

    * Candidate Thinks Out Loud

      * Some strong candidates will know the answer immediately.

      * Strong candidates who don't know the answer immediately will raise a few possibilities. Good example answers include:

        * `first` and `second` might refer to different objects; or

        * Python somehow isn't checking the contents of `first` and `second`.

    * **Note**: Before moving on, tell the candidate that the reason `first` and `second` aren't equal is because lists are sequential and sequences compare [corresponding elements](https://docs.python.org/3/reference/expressions.html#comparisons).

* **Prompt**: If we write a function to check when the contents of the two lists are equal, when do we want it to return `True` and `False`?

  * **Ask If**: Ask this question if your candidate has trouble restating the problem or making sense of how to approach it.

  * **Ask During**: Restate the problem, solution sketch.

  * **Look For:**

    * Candidate Explains Solution Behavior

      * Candidates should be able to explain that a properly implemented function will return `True` if every element appears the same number of times in the second list with no additional numbers, and `False` otherwise.

* **Prompt**: How would this function determine if the contents in the two lists are equal?

  * **Ask If**: Ask this question if your candidate can explain when the function should return `True`, but can't explain how it would work.

  * **Ask During**: Solution sketch.

  * **Look For:**

    * Candidates Explain Steps

      * Candidates should explain that the function should use loops to check if every element in each of the two lists is equal.

      * Strong candidates might point out that we can first sort each list and then use normal list comparison.

## Wrap-Up

Congratulate your candidate for a job well done! Remind them that practicing will make these questions easier over time.

## Solution

The solution is available in [Deep_Equals.ipynb](Solved/Deep_Equals.ipynb).

------

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
