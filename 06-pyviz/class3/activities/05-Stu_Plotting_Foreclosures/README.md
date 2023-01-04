# Plotting Foreclosures

You’re a data analyst for a real-estate startup that wants to find investment opportunities in the Los Angeles market. Because the firm is a startup, it has limited investment capital, and the partners oppose taking any outsized risk as they build their portfolio.

Your task is to use foreclosure data to find a correlation among the number of foreclosures, the involved lenders, the types of foreclosed properties, and the districts. Your analysis aims to determine an investment strategy for the Los Angeles real estate market.

## Instructions

Use the Jupyter notebook file in the `Unsolved` folder to write your code. The `Resources` folder contains the CSV file that you’ll import.

1. Using the `read_csv` function and the Path module, read `2018_Registered_Foreclosure_Properties.csv` from the `Resources` folder, and create the `la_foreclosures_2018` DataFrame.

2. Review the code that creates the `most_foreclosures_df` DataFrame from the `la_foreclosures_2018` DataFrame. The starter file provides this code. Be sure to run this cell as you work through the next steps.

    >**Important** The [Pandas `isin` function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html) was used to filter the `la_foreclosures_2018` DataFrame based on a Python list that includes the five lenders with the most foreclosures: Ocwen Loan Servicing, LLC; Wells Fargo Bank NA; JP Morgan Chase NA; and Nationstar Mortgage LLC.

3. Use the `points` function to plot the data from the `most_foreclosures_df` DataFrame. Include parameters as follows:

    * Use the “Longitude” and “Latitude” columns in the DataFrame as your geospatial data.

    * Set `geo` equal to True to enable the GeoViews integration

    * Set `color` based on the “Lender” column.

    * Set `alpha` to 0.8.

    * Set `tiles` to "OSM".

    * Set `frame_width` to 700.

    * Set `frame_height` to 500.

    * Create a `title` for the plot.

4. Use the `points` function to create a second plot from the `most_foreclosures_df` DataFrame. Keep all the parameters unchanged except as follows:

    * Set the `color` parameter to “Property Type”.

    * Change the `title` parameter to correspond to the new information that you’re plotting.

5. Use the `points` function to create a third plot from the `most_foreclosures_df` DataFrame. Keep all the parameters unchanged except as follows:

    * Set the `color` parameter to “Council District”.

    * Change the `title` parameter to correspond to the new information that you’re plotting.

6. Answer the following questions in the notebook:

    * After reviewing the visualizations, what insights can you gain about the foreclosures in Los Angeles in 2018?

    * Which lender owns the most foreclosed properties?

    * Do the lenders tend to focus on one area or council district in the city, or do they evenly distribute their properties throughout the region?

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
