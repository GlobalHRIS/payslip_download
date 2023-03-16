import streamlit as st
import pdf2image
import pytesseract
import base64
from pytesseract import Output, TesseractError
from functions import convert_pdf_to_txt_pages, convert_pdf_to_txt_file, save_pages, displayPDF, images_to_txt


# Streamlit Dashboard          
st.set_page_config(page_title ="GlobalHRIS", page_icon =":guardsman:", layout ="wide")
st.image("logo.png", width = 200)
st.title("Global HR Implementation Services Limited")
st.subheader("Payslip PDF to Text file")

html_temp = """
            <div style="background-color:{};padding:1px">
            
            </div>
            """

# st.markdown("""
#     ## :outbox_tray: Text data extractor: PDF to Text
    
# """)
# st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
st.markdown("""
    ## Text data extractor: PDF to Text
    
""")
languages = {
    'English': 'eng',
    'French': 'fra',
    'Arabic': 'ara',
    'Spanish': 'spa',
}

with st.sidebar:
    st.title(":outbox_tray: PDF to Text")
    textOutput = st.selectbox(
        "How do you want your output text?",
        ('One text file (.txt)', 'CSV file(.csv)', 'Text file per page (ZIP)'))
    ocr_box = st.checkbox('Enable OCR (scanned document)')
    
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work?
    Simply load your PDF and convert it to single-page or multi-page text.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    
pdf_file = st.file_uploader("Load your Payslip as PDF", type="pdf")
hide="""
<style>
footer{
	visibility: hidden;
    	position: relative;
}
.viewerBadge_container__1QSob{
  	visibility: hidden;
}
#MainMenu{
	visibility: hidden;
}
<style>
"""
st.markdown(hide, unsafe_allow_html=True)
if pdf_file:
    path = pdf_file.read()
    # display document
    #st.write(path)	
    with st.expander("Display document"):
        displayPDF(path)
    if ocr_box:
        option = st.selectbox('Select the document language', list(languages.keys()))
    # pdf to text
    if textOutput == 'One text file (.txt)':
        if ocr_box:
            texts, nbPages = images_to_txt(path, languages[option])
            totalPages = "Pages: "+str(nbPages)+" in total"
            text_data_f = "\n\n".join(texts)
        else:
            text_data_f, nbPages = convert_pdf_to_txt_file(pdf_file)
            totalPages = "Pages: "+str(nbPages)+" in total"

        st.info(totalPages)
        st.download_button("Download Payslip as txt file", text_data_f)
    else:
        if ocr_box:
            text_data, nbPages = images_to_txt(path, languages[option])
            totalPages = "Pages: "+str(nbPages)+" in total"
        else:
            text_data, nbPages = convert_pdf_to_txt_pages(pdf_file)
            totalPages = "Pages: "+str(nbPages)+" in total"
        st.info(totalPages)
        zipPath = save_pages(text_data)
        # download text data   
        with open(zipPath, "rb") as fp:
            btn = st.download_button(
                label="Download ZIP (txt)",
                data=fp,
                file_name="pdf_to_txt.zip",
                mime="application/zip"
		    
     if textOutput == 'CSV file(.csv)':
		    # read text file into pandas dataframe
		    df = pd.read_csv(file, delimiter='\t')
		    # write dataframe to csv file
		    df.to_csv('output.csv', index=False)
		    # display success message
		    st.success('File converted successfully!')
		    with open(file, 'rb') as f:
		    	data = f.read()
		    	b64 = base64.b64encode(data).decode('utf-8')
		    	href = f'<a href="data:application/octet-stream;base64,{b64}" download="output.csv">Download CSV file</a>'
		    	return href    
            )
	



