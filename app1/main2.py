'''
how to run
- open terminal/console and type
- cd app1 
- streamlit run main2.py
'''
from calendar import c
import streamlit as st

st.title("Simple Form")
with st.form('MyForm'):
    name = st.text_input("Enter ur name")
    age = st.number_input("Enter ur age", min_value=18, max_value=90)
    message = st.text_area("Enter your Thoughts")
    time = st.time_input("Enter what time")
    date = st.date_input("Enter the date")
    file = st.file_uploader("Select a file")
    camera = st.camera_input("Grab a photo from webcam")
    sb = st.form_submit_button("Submit")
if sb:
    st.write(name)
    st.write(age)
    st.write(message)
    st.write(time)
    st.write(date)
    st.write(file.name)
    st.write(camera)

with st.form('Another Form'):
    color = st.color_picker("Select ur color")
    num1 = st.select_slider("Select a value",[1,5,10,15,20,25])
    num2 = st.slider("Select another value", min_value=25, max_value=100, step=5)
    gender = st.radio("Gender", ['Male','Female','Other'], horizontal=True)
    education = st.selectbox("Select ur highest education",
        ['Intermediate','High-school', 'Graduate', 'Master', 'Padhe likhe gawar'])
    choices = st.multiselect("Select what u like",
        ['Maggi','Pizza','Spinach','Dry Fruits','Noodles','🍒'])
    is_checked = st.checkbox("Agree to our secret terms and conditions", value=True)
    sb2 = st.form_submit_button("Submit")
