# More Practice with Variables and Conditionals

In this activity, you will get more practice declaring and manipulating variables, as well as using if-else statements.

## Instructions

Open the [starter file](Unsolved/condition-control-flow-02.py) and perform the following:

**Create Character One**

1. Create a variable called `c1_name` and have it equal a string of "Mr. Farley".

2. Create a variable called `c1_age` and have it equal to an integer of 65.

3. Create a variable called `c1_profession` and have it equal to "Web Developer".

4. Create a variable called `c1_salary` and have it equal to 100000.00.

5. Create a variable called `c1_species` and have it equal to "cat".

6. Create a variable called `c1_location` and have it equal to "San Francisco, CA".

7. Create a variable called `c1_monthly_rent` and have it equal to 2000.

8. Create a variable called `c1_monthly_expenses` and have it equal to 1500.

9. Create a variable called `c1_yearly_rent` and have it equal to `c1_monthly_rent` * 12.

10. Create a variable called `c1_yearly_expenses` and have it equal to 1500.00 * 12.

11. Create a variable called `c1_savings` and have it equal to `c1_salary` - (`c1_yearly_rent` + `c1_yearly_expenses`).

**Create Character Two**

1. Create a variable called `c2_name` and have it equal a string of "Mr. Snuggles".

2. Create a variable called `c2_age` and have it equal to an integer of 30.

3. Create a variable called `c2_species` and have it equal to "mouse".

4. Create a variable called `c2_profession` and have it equal to "Accountant".

5. Create a variable called `c2_salary` and have it equal to 70000.

6. Create a variable called `c2_location` and have it equal to "Oakland, CA".

7. Create a variable called `c2_monthly_rent` and have it equal to 4000.

8. Create a variable called `c2_monthly_expenses` and have it equal to 500.

9. Create a variable called `c2_yearly_rent` and have it equal to `c2_monthly_rent` * 12.

10. Create a variable called `c2_yearly_expenses` and have it equal to `c2_monthly_expenses` * 12.

11. Create a variable called `c2_savings` and have it equal to `c2_salary` - (`c1_yearly_rent` + `c2_yearly_expenses`).

**Conditionals**

1. Write an if-else statement to check if `c1_name` is equal to "Mr. Farley".

    * If so, print a string of "Hello Mr. Farley" using the `c1_name` variable.

    * If not, print a string of "Hello stranger".

2. Write an if-else statement to check if `c2_age` is greater than `c1_age`.

    * If so, print a string of "Mr. Farley is older than Mr. Snuggles".

    * Else if `c1_age` is greater than `c2_age`, print a string of "Mr. Snuggles is older than Mr. Farley".

    * Else, `c1_age` must be equal to `c2_age`, therefore, print a string of "Mr. Farley is the same age as Mr. Snuggles".

3. Write an if-else statement to check if `c1_location` is equal to "Oakland, CA".

    * If so, print a string of "Mr. Farley comes from the home of the Raiders!".

    * Else if `c2_location` is equal to a string of "San Francisco, CA", print a string of "Mr. Farley comes from the home of the 49ers!".

    * Else, both conditions must not apply, therefore, print a string of "Mr. Farley doesn't hail from a sports town."

4. Write an if-else statement to check if `c1_rent` is greater than `c2_rent`.

    * If so, print a string of "Mr. Farley pays more rent than Mr. Snuggles".

    * Else if `c1_rent` is less than `c2_rent`, print a string of "Mr. Farley pays less rent than Mr. Snuggles".

    * Else, `c1_rent` must be equal to `c2_rent`, therefore, print a string of "Mr. Farley pays the same rent as Mr. Snuggles".

5. Write an if-else statement to check if `c1_monthly_expenses` is greater than `c2_monthly_expenses`.

    * If so, print a string of "Mr. Farley has more expenses than Mr. Snuggles".

    * Else if `c1_monthly_expenses` is less than `c2_monthly_expenses`, print a string of "Mr. Farley pays less expenses than Mr. Snuggles".

    * Else, `c1_monthly_expenses` must be equal to `c2_monthly_expenses`, therefore, print a string of "Mr. Farley pays the same expenses as Mr. Snuggles".

6. Write an if-else statement to check if `c1_profession` is equal to "Web Developer" AND if `c2_profession` is equal to "Accountant".

    * If so, print a string of "They are a Web Developer and an Accountant".

    * Else, print a string of "They are professionals."

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
