# The Judge's Panel

It's been three weeks, but you've finally heard back from REMAX regarding your job application! Unfortunately, the hiring manager wants you to do one final technical evaluation. The REMAX team has narrowed their choices down to two candidates: you and another developer who has experience working with Tableau.

In order to make their decision, the REMAX team needs to assess your ability to create an analytic platform (dashboard) that satisfies multiple analytic needs.

Put your best foot forward and create a dashboard using Panel. Emphasize to the hiring managers that your programming and analytic skills make you the best fit for this role. Unlike your competition, you can leverage both Python and PyViz (Plotly and hvPlot) to create an interactive, analytic experience.

## Instructions

Use the provided plots to generate your dashboard.

1. Create a Panel **row** using `parallel_categories` and `parallel_coordinates`. Name this object `row_of_parallel`.

2. Create a **row** that contains only `num_foreclosures_plot`. Name this object `row_of_bar`.

3. Use the `append` function to add `num_sales_plot` to the **row** object created in step 2.

4. Create a **column** object that contains a Markdown title, `row_of_parallel`, and `row_of_bar`. Name this object `plots_as_column`.

5. Declare a **tab** object containing the following content: `plots_as_column`, `row_of_bar`, and `row_of_parallel`. Name this object `tabs`.

- - -

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
