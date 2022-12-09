# Palindrome

Write a function that determines if a string argument is a palindrome.

Example:

```python
palindrome("mom")
# Output: True

palindrome("mother")
# Output: False
```

## Notes to the Interviewer

Remember—you are concerned more with the candidate's ability to _communicate_ their approach than with the correctness of their solution. For the purposes of this exercise, both provided solutions are equally acceptable.

If your candidate finds a solution quickly, make them work toward one of the solutions that they did _not_ discover.

## Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: Will this work with strings that have spaces?

  * **Ask If**: What if the test string were:

  ```python
  test = "Never odd or even"
  ```

  * **Ask During**: Solution sketch, implementation discussion.

  * **Look For:**

    * Candidate can confirm yes or no based on their solution.

    * The best candidates will be able to tweak their solutions to allow removal of spaces for the test.
  
* **Prompt**: Is this the only solution?

  * **Ask During**: Solution sketch, implementation discussion.

  * **Look For:**

    * Candidate discusses alternatives.

    * Strong candidates will identify multiple-solution approaches, but it's OK if they don't see more than one.
  
    * What you want to see is that the candidate explains alternative approaches or justifies why no alternative exists.

## Hints

* Write down a palindrome. Can you point out which parts are equal?

  * **Follow-Up**. How would you check if those parts are equal?

* Can you think of a way to check if the front of the word is equal to the back of the word?

  * This is a fairly revealing hint. Only provide it if necessary.

## Solutions

[Palindrome.ipynb](Solved/Palindrome.ipynb).

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
