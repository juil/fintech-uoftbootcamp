# Highest Product of Two

Write a function that accepts a list of integers and returns the largest number we can get by multiplying two of them. For example, for the list:

```python
[-100, 2, 42, 100]
```

...We should get `42 * 100 = 4200`.

## Notes to the Interviewer

This is a good question to pose to candidates who have already seen the [maximin problem](../maximin). Other candidates are more likely to need the hint that they should take a [greedy approach](https://en.wikipedia.org/wiki/Greedy_algorithm).

## Prompts from the Interviewer

* **Prompt**: Can you think of a way to solve this problem with brute force?

  * **Ask During**: Solution sketch.

  * **Ask If**: Ask this question to candidates who have trouble getting started on the question on their own.

  * **Look For:**

    * Candidate Explains Solution

      * The brute force solution is to take every possible product, and then pick the biggest of them.

      * This is very slow for large input lists, so it's not the _best_ answer, but it's a good start.

      * Don't let candidates begin implementing this solution unless it's clear they won't be able to uncover the greedy solution.

* **Prompt**: Let's solve a similar problem. Can you think of a way to find the biggest element in a list?

  * **Ask During**: Solution sketch.

  * **Ask If**: Ask this question to candidates who are having trouble moving past the brute force solution.

  * **Look For:**

    * Candidate Explains Solution

      * You want the candidate to explain that they can keep track of the biggest element they've seen _so far_, and return this as the maximum in the list.

      * If your candidate incorrectly explains how they could sort the list and return the last element, simply explain the answer you were looking for to save time.

* **Follow-Up**:

  * Can we do the same thing with this problem?

  * This is purposefully vague. The hint is that we can find the highest product of two numbers by keeping track of the highest product we've seen _so far_.
  
* **Prompt**: If we're going to solve this by keeping track of the highest product of two numbers we've seen so far, what information do we need to keep track of?

  * **Ask During**: Solution sketch.

  * **Ask If**: Ask this question to candidates who are having trouble imagining how they might implement the greedy solution, or to those who think it's enough to _only_ keep track of the highest product we've seen so far.

  * **Look For:**

    * Candidate Explains Solution

      * Strong candidates will explain that they need to keep track of the highest product of two numbers _and_ the highest number they've seen so far.

      * Particularly strong candidates will also realize they should keep track of the _lowest_ number they've seen so far, but it's okay if they don't.

* **Prompt**. Does your solution work for negative numbers? For example, imagine the input `[-10, -10, 30, 1]`.

  * **Ask During**: Implementation discussion.

  * **Look For:**

    * Candidate Explains Shortcomings

    * Strong candidates will realize they need to account for cases where the product of two negative numbers produces the highest product of two.

    * This is the case that necessitates our keeping track of the lowest number we've seen so far.

## Notes

This is a more complicated example to greedy algorithms than the [maximin](../maximin) problem, and should be considered "a level above" that one. A more difficult example of this approach is [buy low, sell high](../buy_low_sell_high).

## Solution

### Brute Force

[The brute force solution](Solved/brute_force.py) is to check every possible pair (except for pairs of the same numbers) and calculate and return the max product.

------

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
