# import datetime as dt
# import time
# from PIL import Image

import streamlit as st
# from stqdm import stqdm

# @ ----- Page Config -----
st.set_page_config(
    page_title="Bruhhhhh",
    page_icon="👌",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# @ ----- Tabs and Columns -----
st.write("# This is just a test")


# tab1, tab2, tab3 = st.tabs(("Tab1", "Tab2", "Tab3"))

# with tab1:
#     tab1_col1, tab1_col2 = st.columns(2)
#     with tab1_col1:
#         st.write("## First Tab First Column")
#         st.selectbox("City", ["City1", "City2"])
#     with tab1_col2:
#         st.write("## First Tab Second Column")
#         st.selectbox("District", ["District1", "District2"])

# with tab2:
#     tab2_col1, tab2_col2 = st.columns(2)
#     with tab2_col1:
#         st.write("## Second Tab First Column")
#     with tab2_col2:
#         st.write("## Second Tab Second Column")

# with tab3:
#     tab3_col1, tab3_col2, tab3_col3 = st.columns(3, gap="small")
#     with tab3_col1:
#         st.write("## Third Tab First Column")
#     with tab3_col2:
#         st.write("## Third Tab Second Column")
#     with tab3_col3:
#         st.write("## Third Tab Third Column")

# @ ----- Form Inputs with sidebar-----
with st.sidebar:
    st.text_input("Enter your name (max characters 30)",
                  "Ex: John Doe", max_chars=30)
    st.text_input("Enter your username (max characters 15)",
                  "Ex: JohnDoe", max_chars=15)
    st.number_input("Enter a number b/w 10 and 45", 10,
                    45, 10, 1, help="choose b/w 10 and 45")
    st.text_area("Enter some text", "Some texttttttt",
                 height=20, max_chars=100, placeholder="entterrrrrrrrrr")
    st.date_input("Enter a date")
    st.time_input("Enter a time")
    st.file_uploader("Upload a file", type=[
                     'png', 'pdf', 'jpg'], accept_multiple_files=True)


# @ ----- Actual form - ----
with st.form("my_form"):
    st.write("Inside the form")
    text_input_val = st.text_input("Form Text Input")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, ", text input",
                 text_input_val, ", checkbox", checkbox_val)


# @ ----- Media Elements -----
# st.image()
