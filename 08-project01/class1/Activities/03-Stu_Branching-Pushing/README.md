# Git Branching/Pushing

In this activity, we will create a new branch, implement a feature, and then submit a pull request back into the main. We will also cover reviewing pull requests and merging them into the main.

# Instructions

## Part I: Branching and Submitting a Pull Request

* In this section, we will create a branch, add a feature, and submit a pull request. **Only one group member should complete this section, everyone else should observe.**

* Clone the project repo onto your computer and use the cd (change directory) command to get into it.

* Run the following command in your terminal to create and checkout to a new branch:

  `git checkout -b add-new-python-script`

* You should now be on a new branch named "add-new-python-script." In order to verify that this worked, run the following command in your terminal:

  `git branch`

* You should see two branches listed: `main` and `add-new-python-script`. The `add-new-python-script` branch should have an asterisk to the left of it. This indicates that this is the branch you're currently on.

* At the root of the repo, create a new file named `data_collection.py`. Inside this file, add code to import the `requests` library and save.

* In your terminal, add and commit the changes. Then push up your code by running the following in your terminal:

  `git push origin add-new-python-script`

* This should push up your code to GitHub on a branch with the same name (`add-new-python-script`).

* Go to the main repo page at github.com and you should see an button that says "Compare & pull request." Click this.

<img alt=01-Recently-Pushed.png src=Images/01-Recently-Pushed.png width=600>

* On the next screen, add a description of the work that was done in the text area and click the "Pull Request" button.

<img alt=02-Pull-Request.png src=Images/02-Pull-Request.png width=500>

* If completed successfully, you should see the pull request listed under the repo's "Pull request" tab.

## Part II: Reviewing a Pull Request

* In this section, we will review the pull request from Part I and merge it into the main. **A different project member should complete this section while others observe**.

* Clone the repo to your computer if you haven't already done so, and use the cd command to get into it.

* First, you will want to test the changes introduced by the `add-new-python-script` branch locally. To examine the new branch on your local machine, run the following commands in your terminal:

  `git fetch --all`

  `git checkout add-new-python-script`

* This code should bring the copy of the `add-new-python-script` branch that's on GitHub onto your computer.

  * Make sure this worked by verifying that there's an `data_collection.py` file in your local repo.

  * Typically, you would run the code here to make sure everything works properly.

* Check back out to your local `main` branch by running the following in your terminal:

  `git checkout main`

* Now go to your GitHub repo's main page and go to the "Pull request" section. Select the `add-new-python-script` pull request from the list.

<img alt=03-PR-List.png src=Images/03-PR-List.png width=600>

* On the next page, select the option to see the "Files changed."

<img alt=04-Review.png src=Images/04-Review.png width=500>

* You should be presented with all of the files that were changed in this PR, along with line numbers for any code added or removed.

<img alt=05-Files-Changed.png src=Images/05-Files-Changed.png width=500>

* If there are any changes you would like made, you can click the line number to leave a comment the PR author will see and should address before approval. Otherwise click "Review changes" and approve the PR. You should be taken to a screen with an option to "Merge pull request." Click this button.

<img alt=06-Approve.png src=Images/06-Approve.png width=500>

* Once complete, you can delete the feature branch from your machine by running the following in your terminal:

  `git branch -D add-new-python-script`

* Ask an instructor or TA if you get stuck or have any questions!

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

