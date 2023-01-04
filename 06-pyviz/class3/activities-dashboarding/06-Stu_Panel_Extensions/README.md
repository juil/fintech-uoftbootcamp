# Extending Plotting

It's time to extend your plotting skills. Over the past two lessons, you've learned how to create a range of interactive plots using hvPlot and **Plotly Express**; however, you haven't had one centralized location to embed these plots. Now, you do!

Use Panel as a foundation for extending your plotting skills by creating a Panel dashboard that leverages **Mapbox** and hvPlot to visualize real estate data geographically. The end product of this activity will be a dashboard that includes both **hvPlot** and **Plotly Express** visualizations.

Once finished, you'll have officially integrated multiple plot types on one dashboard, as well as extended beyond one-dimensional approaches of reporting.

If you finish early, assist your peers with troubleshooting and debugging.

## Instructions

1. Create a `.env` with your Mapbox API stored as the environment variable `mapbox`.  

2. Use the Panel `extension` function to specify the Panel plugin(s) required for today's activity. The activity will use **Plotly Express** and **hvPlot**.

3. Using the code provided:

    * Read in your Mapbox API key.
    * Set the Mapbox access token.
    * Read in CSVs and prepare the data.
    * Create the plots.
    
    
4. Create a Panel column and add `population_plot` and `crime_plot` to it. Also, provide a Markdown header explaining what these plots represent.

   **Hint:** `## Population and Crime Geo Plots`.

5. Create a second Panel column and add `population_violence` and `violent_murder` objects to it. Provide a markdown header.

6. Create a tabs object that will contain the column panels created in steps 1 and 2. There should be two tabs, with a column object in each.

7. Customize the labels used for each tab. The first tab should be called **Geospatial**. The second should be called **Correlations**.

### Hint

Make sure the plots are displayed correctly. This means using the appropriate widths and zooms (i.e., for Mapbox plots). Both of these can be configured using the `width` and `zoom` attributes, respectively.

- - -

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
