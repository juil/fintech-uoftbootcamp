# Maximin

Write a function that prints the minimum and maximum elements from a list *without* using the `min` or `max` list functions.

```python
[12, 33, 41, 2, 61, 32, 75, 43, 67]
```

## Notes to the Interviewer

The solution to this problem is simple enough that most candidates will immediately understand the code, but producing it requires them to realize they should write a [greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm).

Candidates are not allowed to use the list `min` or `max` because it is possible to write a strictly _faster_ solution than calling these built-in methods.

## Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee.

* **Prompt**: Before you think about finding both the minimum _and_ the maximum, can you first explain how you'd find the maximum?

  * **Ask During**: Solution sketch.

  * **Look For:**

    * Candidate Explains Solution

      * There are at least two common solutions to this problem.

      * Candidates should explain that they can sort the list, and take the last element from the sorted list as the maximum; this is both clever and correct. If your candidate takes this approach, commend them for their ingenuity, but let them know that there is a _faster way_.

      * Candidates should explain that they can look at every element in the list, starting with the first, and "remember" the biggest element they've seen so far.

      * Strong candidates will immediately explain that they can take the same approach to find the minimum.

* **Prompt**: Can you find the minimum and maximum at the same time?

  * **Ask During**: Solution sketch.

  * Candidate Explains Solution
  
    * Yes, we can find the minimum and maximum at the same time. We keep track of the minimum so far _and_ the maximum so far in our `for` loop—there is no need to loop through twice.

    * Particularly strong candidates will identify that calling `min` and `max` functions requires us to read the list twice—once for each function call.

## Notes

This is an exemplary introduction to greedy algorithms—algorithms that keep track of the _best answer so far_. More difficult examples of this approach include the [buy low, sell high](../buy_low_sell_high) and [highest product of two](../highest_product_of_two) questions.

## Solution

### Linear Scan

[The linear scan solution](Solved/maximin.py) is to scan the list once and keep track of the minimum and maximum numbers.

------

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
