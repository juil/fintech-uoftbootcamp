# Fizz Buzz

Write a script that prints the numbers 1 to 100 in the console. For multiples of three, print `Fizz` and for multiples of five, print `Buzz`. For numbers that are multiples of both three and five, print `FizzBuzz`.

## Notes to the Interviewer

This is a common screening question. There is no need to drill your candidate on details with this problem.

## Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: Does the order in which we check if our number is a multiple of three, five, or both matter?

* **Ask During**: Solution sketch, implementation discussion.
  
* **Look For:**

  * Candidate Explains Solution

    * It does matter. The candidate should be able to reason through why if you raise this during the sketch phase, or explain the error in their code if you raise it during the discussion phase.

## Hints

Remember the Pythons `%` modulo operator!

## Solution

### Modulo If-Else Statements

The solution is simply to check that the current number is a multiple of both three and five; then check whether the number is a multiple of three; then check whether the number is a multiple of five; and then just print the number if all else is false.  A solution to this problem can be found [here]

The solution file is available in [solution.py](Solutions/solution.py).

------

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
