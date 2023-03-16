import streamlit as st
import pandas as pd

def convert_to_csv(file):
    # read text file into pandas dataframe
    df = pd.read_csv(file, delimiter='\t')

    # write dataframe to csv file
    df.to_csv('output.csv', index=False)

    # display success message
    st.success('File converted successfully!')

# Streamlit app
def app():
    st.set_page_config(page_title="Text to CSV Converter")
    st.title("Text to CSV Converter")

    # file upload widget
    file = st.file_uploader("Upload a text file", type=["txt"])

    # convert file to csv on button click
    if st.button("Convert to CSV"):
        if file is not None:
            convert_to_csv(file)
        else:
            st.warning("Please upload a text file first.")
