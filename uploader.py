import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader(
    label="Choose a file",
    type="txt")

if uploaded_file is not None:
    try:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        #st.write(bytes_data)
    except:
        pass

    try:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        #st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        #st.write(string_data)
        if "area" not in st.session_state:
            st.session_state.value = None
        if len(string_data) > 0:
            st.session_state.value = string_data
        else:
            st.session_state.value = None
        txt = st.text_area(label="Texto lido", value=st.session_state.value,
                       height=300, max_chars=1000,
                       key='area', help="Digite ou cole aqui seu texto")
        if txt:
            nTxt = len(txt)
            nWord = len([t for t in txt.split() if t.strip() != ''])
            st.markdown(f"*:red[Número de caracteres]: {nTxt}")
            st.markdown(f"*:blue[Número de palavras]: {nWord}")
            st.markdown(f"*:brown[Arquivo]: {uploaded_file.name}")
    except:
        pass

    try:
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        #st.write(dataframe)
    except:
        pass


uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
