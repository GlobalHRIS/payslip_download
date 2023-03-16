import streamlit as st
import pandas as pd
import base64

def convert_to_csv(file):
    # read text file into pandas dataframe
    df = pd.read_csv(file, delimiter='\t')

    # write dataframe to csv file
    df.to_csv('output.csv', index=False)

    # display success message
    st.success('File converted successfully!')

    return 'output.csv'

# function to create download link
def get_download_link(file):
    with open(file, 'rb') as f:
        data = f.read()
        b64 = base64.b64encode(data).decode('utf-8')
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="output.csv">Download CSV file</a>'
    return href

# Streamlit app
def app():
    st.set_page_config(page_title="Text to CSV Converter")
    st.title("Text to CSV Converter")

    # file upload widget
    file = st.file_uploader("Upload a text file", type=["txt"])

    # convert file to csv on button click
    if st.button("Convert to CSV"):
        if file is not None:
            file_path = convert_to_csv(file)
            st.markdown(get_download_link(file_path), unsafe_allow_html=True)
        else:
            st.warning("Please upload a text file first.")
