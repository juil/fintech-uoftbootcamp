# It's a Map Plot

It's time to take a break from your day job and plan an adventure!

Your friends have decided to plan a group trip to New York City for Harold's birthday. In planning for the event, you've started doing some research regarding points of interest in NYC. You've found one dataset that lists a bunch of cool places to see.

Use Plotly Express and **MapBox** to create a geographical plot that will visualize each area of interest within the city. If you finish early, complete the challenge section.

### Instructions

1. Read in the **Mapbox API key** using the `os.getenv` function.

2. Read in the places of interest data.

3. Use the Plotly Express `scatter_mapbox` function to plot interest data, setting the colour to **Name** with the `color` attribute.

4. Use `scatter_mapbox` to plot places of interest by **place type**.

5. Plot places of interest by **borough**.

6. Review the data and identify three different types of places from the plots that you'd like to visit. Make sure these places are within walking distance.

### Challenge

1. Plot parks that are of interest.

2. Plot gardens that are of interest.

3. Plot squares that are of interest.

### Hint

Creating too many map plots in one notebook might create a memory issue. Consider creating a separate notebook for the challenge section. This will require you to read the CSV data in both notebooks.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
