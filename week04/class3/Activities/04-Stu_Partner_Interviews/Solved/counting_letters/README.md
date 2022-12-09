# Counting Letters

Write a function that counts how many times each letter in a string occurs.

For example:

```python
test = "Example sentence"
count_letters(test)
```

Output

```sh
{'E': 1,
 'a': 1,
 'c': 1,
 'e': 4,
 'l': 1,
 'm': 1,
 'n': 2,
 'p': 1,
 's': 1,
 't': 1,
 'x': 1}
```

## Notes to the Interviewer

There are multiple solutions to this problem, but we are particularly interested in students identifying **dictionaries** as the appropriate data type for this problem.

## Prompts from the Interviewer

* **Prompt**: Is your function case-insensitive? That is, does it treat 'E' and 'e' the same way?

  * **Ask During**: Solution sketch, implementation discussion.

  * **Look For:**

    * Candidate Discusses Possibilities

      * Candidates should identify whether their function appropriately deals with capitalization.

* Most commonly, this entails calling `lower()` on the sentence.

## Solution

One solution for this exercise is available in [Counting_Letters.ipynb](Solved/Counting_Letters.ipynb).

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
