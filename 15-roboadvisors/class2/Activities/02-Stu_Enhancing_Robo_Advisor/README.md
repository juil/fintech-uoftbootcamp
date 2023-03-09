# Enhancing the Bitcoin Fear & Greed Robo Advisor

In this activity, you’ll create an AWS Lambda function to enhance the Bitcoin Fear & Greed robo advisor that you created before. This function will get the current "Bitcoin Fear & Greed Index" by using the [Alternative.me crypto API](https://alternative.me/crypto/fear-and-greed-index/). And, it will get the current price of a bitcoin by using the [Bitcoin price lookup endpoint](https://api.alternative.me/v2/ticker/bitcoin/?convert=USD) of that API.

## Instructions

1. Log in to the AWS Management Console with your IAM administrator user. Then in the “AWS services” search box, type Lambda, and then click Lambda.

2. In the Lambda console that appears, in the left navigation menu, click Functions, and then click the "Create function" button.

3. On the “Create function” page that appears, select the "Author from scratch" option, and then fill in the following information:

    * Function name: getFGIndex

    * Runtime: Python 3.7

4. Click the "Create function" button.

5. Scroll down to the "Code source" section, and then paste the provided starter code from the code editor in the Lambda console.

    **Note:** You might have to double-click the `lambda_function.py` file in the Environment pane to open the editor.

6. Inspect the code of the `get_df_index` and `get_recommendation` functions to understand how the "Bitcoin Fear & Greed Index" is retrieved and how the recommendation is made.

    **Important:** Recall that the names of both the intent and the slots are case sensitive. So, ensure that the names in the Lambda function code match those in the bot that you created before.

6. Click the Deploy button.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.