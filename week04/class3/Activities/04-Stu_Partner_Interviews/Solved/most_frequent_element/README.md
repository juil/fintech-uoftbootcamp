# Most Frequent Element

Write a function that finds the most frequent element in an array.

```python
num_list = [1, 2, 2, 3]

most_frequent(num_list) # Should return 2
```

## Prompts from the Interviewer

* **Prompt**: Does your approach work if two elements appear the same number of times, as in `[1, 2, 2, 3, 3]`?

  * **Ask During**: Solution sketch, implementation discussion.

  * **Look For:**

    * Candidate discusses shortcomings.

      * Certain implementations will return _one_ of the most frequently occurring elements, but not _all_ of them.

      * Strong candidates will explain that properly dealing with the case of multiple frequent elements requires a _loop_ that collects every element that occurs `max` number of times. In the example above (`[1, 2, 2, 3, 3]`), this loop would identify every element occurring twice: `2` and `3`.

* **Prompt**: How does your solution behave if every element occurs the same number of times?

  * **Ask During**: Solution sketch, implementation discussion.

  * **Look For:**

    * **Candidate Asks for Input**.

      * There are multiple legitimate ways to deal with this. One could:

        * Return every element; or

        * Return some value indicating that there is no "most frequent."

      * Both are valid solutions, but the latter is arguably better.

      * Strong candidates will choose one but explain the tradeoffs between the two choices; or they will ask the interviewer what they prefer.

## Hints

* Does your solution change if the input list is unsorted?

  * It shouldn't. A properly implemented solution should work on unsorted lists.

## Solutions

[Most_Frequent.ipynb](Solved/Most_Frequent.ipynb)

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
