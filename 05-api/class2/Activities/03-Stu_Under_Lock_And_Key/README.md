# Under Lock and Key

You and Harold have developed a Python application that will extract historical stock data from **Nasdaq** for a given ticker and calculate the Sharpe ratio for that stock. So far, only you two have been using the program, but your manager now wants you to open the application up to the entire team. You know that Nasdaq allows API calls to be submitted without an API key, but the limit is 50 calls a day. Nasdaq is diligent in their rate-limiting and keeps services under lock and key.

Since Nasdaq has cracked down on the number of API calls users can make to the service without an **API key**, acquire a Nasdaq API key and save it as an **environment variable**. Create Python code that retrieves the environment variable and passes the key with the request URL. This will ensure that your team can make more than 50 API calls a day, and Nasdaq can manage and track rate limits.

## Instructions

### Acquire and Store API key

1. Navigate to the Nasdaq [Account Settings](https://data.nasdaq.com/account/profile) page to retrieve your API key.

2. Create a new `.env` file, and declare an environment variable named `NASDAQ_API_KEY`.

3. Open the [Jupyter Notebook starter file](Unsolved/env_variables.ipynb), and import the Python `requests`, `os` and `dotenv` libraries.

### Execute API call with API key/env variable

4.  Use the `load_dotenv()` method from the `dotenv` package to load and export the environment variables.

5. Use the `os.getenv()` function to retrieve the environment variable named `NASDAQ_API_KEY`, and store it as a Python variable named api_key.

6. Use the `type` function to confirm the retrieval of the API key. Hint: If `NoneType` is returned, the environment variable does not exist. Revisit steps 2 and 3.

7. Concatenate **request_url** with the **api_key** variable.

8. Execute a `GET` request using Python requests library and the newly created request_url.

9. Display content to screen using the content attribute.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
