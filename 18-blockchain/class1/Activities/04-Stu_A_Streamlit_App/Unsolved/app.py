# @TODO: Import the libraries for Pandas and Streamlit
import streamlit as st
import pandas as pd

# @TODO: Create a title for your application using markdown syntax and the
# Streamlit `write` function.
st.write("# Streamlit Application")

# @TODO: Create an opening sentence for your application using regular text and
# the Streamlit `write` function.
st.write("We are **LIVE**")

# @TODO: Create a Pandas dataframe
df = pd.DataFrame({'name': ['Juil', 'Yogurt', 'Conda']})

# @TODO: Write the Pandas dataframe to the page
st.write(df)

# @TODO: Create a text input box using the Streamlit `text_input` function.
# @TODO: Save the input as a variable.
new_username = st.text_input("User Name:")

# @TODO: Utilize the Streamlit `button` function to display the text input
# variable created in the prior step to the page.
if st.button("Add"):
    new_user = {'name': new_username}
    df.loc[len(df)] = new_user
    st.write(f"{new_username} added.")
    st.write(df)

# Bonus
# YOUR CODE HERE!
