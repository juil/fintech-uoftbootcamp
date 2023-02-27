# Create a Short-Position Algorithm

In this activity, you’ll create an algorithm to identify the entry and exit points for a short-position trading strategy. The algorithm will still use a short-window (50 days) SMA and a long-window (100 days) SMA.

This is a mini-project activity intended to be done by groups of two or three people.

## Background

The real-estate bubble that led to the financial crisis in 2008 resulted in one of the worst economic disasters since the Great Depression of 1929. During this period, housing prices fell precipitously. This caused massive ripples throughout the US economy and ultimately caused the stock market to crash. Some investors profited from the recession by shorting the market, or placing bets that the market would fall. Most, however, lost substantial value from their investment portfolios, including much-needed retirement and savings accounts.

If you had an algorithm to monitor and short the market in 2008, when a collapse in the financial derivatives markets led to a historic economic downturn, would you have made money? Your task in this activity is to create a DMAC strategy that would have shorted VNQ stock, which is a real-estate exchange-traded fund (ETF), from 2007 to 2009.

> **Hint:** Remember that taking a short position (that is, making a profit from selling) is the opposite of taking a long position (making a profit from buying). Make sure that the decision logic for creating your trading signals reflects this.

## Instructions

The instructions for this activity are divided into the following subsections:

* Create a DMAC Trading Signal

* Plot the Entry and Exit Points of the Trading Signal

### Create a DMAC Trading Signal

To create a DMAC trading signal that indicates shorting opportunities, complete the following steps:

1. Read the `vnq.csv` file from the `Resources` folder into a Pandas DataFrame. Set the “Date” column as the index. Review the DataFrame.

2. By filtering the DataFrame, create a second DataFame, named `signals_df`, that contains only the “Date” index and the “Close” column. Review the new DataFrame, and then use hvPlot to visualise the pricing information.

3. Set the `short_window` and `long_window` variables to 50 and 100, respectively.

4. Using the “Close” column as well as the `rolling` and `mean` functions, create columns named “SMA50” and “SMA100” that contain the 50-day and 100-day simple moving averages, respectively. Review the DataFrame.

5. Create a new column, named “Signal”, in the DataFrame, and set all its values to 0.0.

6. Using the NumPy `where` function, set the “Signal” column to 1.0 when the “SMA50” value is less than the “SMA100” value. Otherwise, set the “Signal” column to 0.0. Review the DataFrame.

7. Use the Pandas `diff` function on the “Signal” column to assign values of 1 or &minus;1 to the “Entry/Exit” column. These values will indicate the trade entry and exit points in time. Review the DataFrame.

### Plot the Entry and Exit Points of the Trading Signal

To plot the entry and exit points of your short DMAC trading signal, complete the following steps:

1. Using hvPlot, create two scatter plots: one for the entry points and another for the exit points. Use purple markers to indicate the entry points (when the algorithm sells the stock). Use orange markers to indicate the exit points (when the algorithm buys the stock to cover the short position).

    > **Hint:** Remember that you’re creating a short-position algorithm. The signal to trade (1) occurs when the short-window SMA (the “SMA50” value) is less than the long-window SMA (the “SMA100” value).

2. Create two line plots: one for the VNQ closing prices and another for the 50-day and 100-day SMAs.

3. Combine all four plots from Steps 1 and 2 into one overlay plot.

    > **Hint:** For more information, refer to [Composing Plots](https://holoviz.org/tutorial/Composing_Plots.html) in the HoloViz documentation.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
