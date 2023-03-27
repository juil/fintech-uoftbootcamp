# A Streamlit App

In this activity, you will use the [Streamlit library](https://docs.streamlit.io/en/stable/index.html) to build a web application.

## Instructions

Complete the following steps. If you have already installed the Streamlit library on your machine, proceed to Step 3. Otherwise, begin with Step 1.

1. Open a terminal instance and activate your Conda `dev` environment.

2. Install the Streamlit library by using the following code:

  ```shell
  pip install streamlit
  ```

3. Open the `app.py` starter file in the Visual Studio Code IDE.

4. Import the libraries for Pandas and Streamlit

5. Create a title for your application using Markdown syntax and the Streamlit `write` function.

6. Create an opening sentence for your application using regular text and the Streamlit `write` function to display the sentence on the application page.

7. Create a Pandas DataFrame, and then use the Streamlit `write` function to display the DataFrame to the page.

8. Create a text input box using the Streamlit `text_input` function. Save the input as a variable.

9. Use the Streamlit `button` function to display the text input variable (created in the previous step) to the page.

10. Navigate to the terminal instance. From the folder containing your `app.py` file, run the Streamlit web application by using the following code:

  ```shell
  streamlit run app.py
  ```

## Bonus

If you complete the activity early, add other elements to your page, such as `text_area`, `sidebar`, and `select_box`. You can learn about these elements in the [Streamlit documentation](https://docs.streamlit.io/en/stable/index.html).

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
