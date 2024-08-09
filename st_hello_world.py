import streamlit as st

st.write("Hello World!")

#boton

st.header("st.button")

if st.button("Decir Hola"):
    st.write("Hola Rey, como estas?")
else:
    st.write("Ni nos vimos")
    