'''
how to run
- open terminal/console and type
- cd app1 
- streamlit run main.py
'''

import streamlit as st

st.title("This is A title")
st.header("This is Heading")
st.subheader("Subheading")
st.text("A very normal text on a normal day")
st.write('This is the magic function to write stuff')
st.success("This is text written for success messages")
st.error("This is text written for error messages")
st.info("this is information message text")
st.warning("This is a warning text")
st.markdown('''
this is a markdown text, here u are free to use
<h5> HtML <h5>
<p> this is a paragraph </p>
<ul>
    <li> One two</li>
    <li> Three Four</li>
    <li> Five Six</li>
</ul>
or 
# Markdown heading
''', unsafe_allow_html=True)
st.code('area where we can put code')