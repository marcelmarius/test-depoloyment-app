import streamlit as st


st.write('App Title')

selected = st.radio("chose Your Star", [1,2])

if selected == 1:
    st.write("You selected the button: 1")

if selected == 2:
    st.write("You selected the button: 2")