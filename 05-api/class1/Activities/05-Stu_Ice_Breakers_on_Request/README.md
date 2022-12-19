# Ice Breakers on Request

Your company has recently begun engaging in table talk sessions aimed towards helping the team continue to build soft and conversational skills by having co-workers engage each other about various financial topics for 5 minutes. Your goal is to have financial ice breakers available on request. You've found 4 APIs that you feel could provide some good material for table/small talk.

Submit `GET` requests using the Python `requests` library for one of the below `request urls`. Then, interpret the JSON output and save a fact or other value from the JSON output, as a variable.

APIS

* Current Bitcoin Prices -> https://api.coindesk.com/v1/bpi/currentprice.json

* Exchange Rates ->  https://open.er-api.com/v6/latest/CAD

* The Daily Releases of Statistics Canada: <https://www150.statcan.gc.ca/n1/dai-quo/ssi/homepage/daily-banner-eng.json>

* Canadian GDP Data: <http://api.worldbank.org/v2/country/ca?format=json>

## Instructions

1. Choose one of the above APIs to work with for this assignment.

2. Execute the `requests.get` function using one of the `request urls`, and store the output in a variable named `response_data`.

3. Retrieve the status code of the request.

4. Execute `response_data.content` to extract the data from the request. Store the data in a variable named `response_content`, and output the data to the screen.

5. Use the `json` function to format `response_content` as JSON. Store the output as a variable named `data`.

6. Import the `json` package, and use `json.dumps` to print `response_content` to the screen with formatting. Use the `indent=4` parameter to format with indentation.

7. Decipher the JSON data, then select an element from the JSON and store it into a new variable. Hint: JSON attribute names are like keys in dictionaries.

### Challenge

If time remains, use the `GET` function to explore the other APIs.

### Hint

Selecting values from JSON data requires data be accessed first by parent object and then child. When an API returns output with multiple `JSON Objects`, `indices` have to be specified to indicate which object/record should be selected. For example,

  ```python
  selected_value = data['all'][0]['text']
  ```

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
