# I Spy an API

You've received an e-mail from your Python mentor, Julia. Read the e-mail below and see if she has any new tasks for you.

> Good Morning Mentee,
>
> I was going through some old documents and came across this list of FinTech APIs I did some research on when implementing a Monte Carlo portfolio simulation (see attached). They're nothing too fancy, but you could use them if you're ever in a bind and need to get some financial data quick. I've included brief descriptions of what each API does.
>
> Full disclosure: I haven't checked these APIs out in a while. I'd suggest testing them out to see if they're still functioning. Let me know your findings.
>
> All the Best,
>
>Julia

APIs to Investigate:

* Nasdaq Data Link is a service that provides historical stock data. For example, this API would be useful if you needed to calculate cumulative returns for `GOOG`.

  > https://data.nasdaq.com/api/v3/datasets/WIKI/GOOG.json

* The World Bank API has a wealth of international bank data. For example, if you wanted to analyze the growth rate of each country's gross domestic product values (GDP), you could extract GDP values, by year, from the World Bank API.

  > http://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json

* If you wanted only one country, like Canada, you can change the query slightly, from `all` to just `ca`:

  > http://api.worldbank.org/v2/country/ca/indicator/NY.GDP.MKTP.CD?format=json

* Coinbase provides price data for cryptocurrencies through their API. Use the Coinbase API if you need to get the price of a crypto for any given moment, such as `BTC`.

  > https://api.coinbase.com/v2/prices/BTC-CAD/buy?format=json

## Instructions

Using `Postman`, submit `GET` requests to the above APIs using the provided request URLs. Confirm that a response has been received from the servers.

It is recommended that you save each API request and the output so that it can be leveraged for future assignments.

1. Get `GOOG` stock data using `Nasdaq API`.

2. Get `GDP` data for the `US` using `World Bank API`.

3. Get the current `Bitcoin` price using `Coinbase API`.

The TAs will be circulating during this activity. Do not hesitate to reach out for assistance if you experience any trouble using `Postman` or any of the APIs.

Let the TAs know once you've finished the core activity. If time still remains, give the challenge section a try.

### Challenge

1. Change the above `Nasdaq` request URL to query for `AMD` instead of `GOOG`.

2. Update the `Coinbase` request URL to query for `ETH-CAD` instead of `BTC-CAD`.

3. Use the `Nasdaq API` to get `GOOG` stock data in `CSV` format. Take note of how the change in URL alters the format (json vs csv) of the data returned by the API.

### Hint

The output format of an API can be changed by altering the `?format=` part of the link, or changing the extension of the target file from `json` to `csv`. See below for examples.

* Nasdaq -> https://data.nasdaq.com/api/v3/datasets/WIKI/GOOG.json

* Nasdaq -> https://data.nasdaq.com/api/v3/datasets/WIKI/GOOG.csv

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
