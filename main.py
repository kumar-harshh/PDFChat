import streamlit as st

st.title("Chat with multiple PDFs 👋🏻")
st.text_input("Hi! How May I Help?")
with st.sidebar:
    st.header("Upload your PDFs 📚")
    st.file_uploader("Select your PDF files & Click on 'Process' to proceed")
    st.button("Process")










#Streamlit Basic tutorial


# import pandas as pd
# import time

# # Display text, data, and objects.
# st.write("Hello, Streamlit!")
# st.write() 

# #Display titles and headers.
# st.title("My Streamlit App")
# st.header("Chat with Multiple PDF")
# st.subheader("Now you can chat with your complex documents, Snap") 

# # Display plain text.
# st.text("Lorem Ipsum")

# #Displaying Data:
# #DataFrame

# data={
#     'Name':['Harsh', 'Tua', 'Ashish', 'Anmol'],
#     'Age':[23,22,21,31],
#     'City':['BLR', 'KOAA', 'KOAA', 'BLR']
# }

# df=pd.DataFrame(data)
# st.dataframe(df)# Display a DataFrame.

# #Table Data

# table_data=[
#     ['Harsh', 23, 'BLR'],
#     ['Tua', 22, 'KOAA']
# ]
# st.table(table_data)# Display a static table.

# #JSON Data

# json_data={
#     "Name":"Harsh",
#     "Age":23,
#     "City":"BLR",
#     "Hobbies":["Cooking", "Cricket", "Reading Books"]
# }

# st.json(json_data)# Display JSON data.

# #Interactive Widgets:

# #: Create interactive widgets.
# st.button("Label: Click Here")
# st.checkbox("Label: Checklist1")
# st.checkbox("Label: Checklist2")

# st.radio("Radio", ["Tag1", "Tag2", "Tag3"])
# st.selectbox("Dropdown", ["Option1", "Option2", "Option3"])

# # Create sliders and selectors.
# st.slider("Slider", 0,10)
# st.select_slider("Select Slider", ["Option1", "Option2", "Option3"])
# st.multiselect("Multi Select", ["Option1", "Option2", "Option3"])

# #: Accept user inputs
# st.text_input("Text Input: Enter Text")
# st.number_input("Number Input: Enter a Number")
# st.text_area("Text Area")

# #Adding Sidebat
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# #Progress Bar
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

