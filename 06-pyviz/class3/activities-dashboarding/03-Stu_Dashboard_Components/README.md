# No Pane, No Gain

It's time to get some experience working with PyViz objects in Panel. Panes are the fundamental building block of any Panel Dashboard, and without Panes, there can be no dashboard, which means there's no value added. Use the knowledge and skills learned from the instructor demo to convert a Plotly plot to a Panel **pane** object.

## Instructions

Open the starter file.  A function named `create_parallel_categories_plot` has been provided. 

1. Notice that this function performs the following tasks:
    
    * Builds a DataFrame to house randomly generated, fictitious real estate data.
    * Accepts an argument called `number_of_records`.
    * Returns a parallel categories plot made from the data named `metro_prop_sale`.
    
    
2. Visualize the data by making a call to the function `create_parallel_categories_plot`, passing the integer `30` as the argument.
    
### Create Pane Using Interact Function

3. Use the `interact` function to create an interactive widget **pane**:

    * Pass `create_parallel_categories_plot` function to `interact.` 
    * Set `number_of_records` to equal `30`.
    * **Hint:** `interact(function_name, function_parameter=30`).


### Create Pane Using panel.pane.Plotly Function

4. Manually convert the `metro_prop_sale` object to a **pane** using the `panel.pane.Plotly` function to convert.

    * **Hint:** You will need to use the `create_parallel_categories_plot(`30`)` function. Store this as `plot_panel`.


5. Use the `panel.pprint` function to ensure the `plot_panel` object is a **pane**.

- - -

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
