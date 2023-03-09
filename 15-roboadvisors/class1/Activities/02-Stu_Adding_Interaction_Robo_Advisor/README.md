# Adding User Interaction to the Robo Advisor

In this activity, you’ll add user interaction to the Bitcoin Fear & Greed Robo Advisor that you created earlier. Specifically, you’ll create an intent, add a slot, and add confirmation prompts.

## Instructions

The instructions are divided into the following three steps:

1. Create the intent.

2. Add a slot.

3. Add the confirmation prompts.

### Step 1: Create the Intent

1. Add a new intent, and name it `getFGIndex`.

2. Define some sample utterances. Start by adding the following:

    * I want to invest in bitcoin

    * I want to buy bitcoin

    * How is the bitcoin market feeling today

### Step 2: Add a Slot

Add a slot with the following configuration:

* Name: amount

* Slot type: AMAZON.NUMBER

* Prompt: How many dollars do you want to buy?

  **Important:** Make sure to select the Required checkbox for the slot.

### Step 3: Add the Confirmation Prompts

In the "Confirmation prompt" section, add the following confirm and cancel prompts.

* Confirm prompt: Are you sure you want to buy ${amount} dollars in bitcoin?

* Cancel prompt: Okay, let's start again.

---

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.