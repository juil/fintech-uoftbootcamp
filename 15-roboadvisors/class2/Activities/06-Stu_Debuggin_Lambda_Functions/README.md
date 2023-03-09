# Debugging Lambda Functions

In this activity, you’ll add test events to test and debug the `getFGIndex` Lambda function that you created before.

## Instructions

1. Log in to the AWS Management Console with your IAM administrator user. Then in the “AWS services” search box, type Lambda, and then click Lambda.

2. In the Lambda console that appears, open the `getFGIndex` function, and then move to the code editor.

3. Create a test event by using the provided `correctAmount.json` file. Note that this test event will successfully fulfil the intent.

    **Important:** Recall that the names of both the intent and the slots are case sensitive. So, ensure that the names in the provided file match those in the bot that you created before.

4. Use the test event to test your Lambda function. Fix any bugs.

5. Create a test event that will cause an error. For example, set a negative or a zero number of dollars to convert to bitcoins.

6. Test your Lambda function. Fix any bugs.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
