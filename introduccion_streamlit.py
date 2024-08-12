import streamlit as st
import random

st.sidebar.title("Menu")
opcion = st.sidebar.selectbox("Elije una pagina", ["Introduccion","Ahorcado"])

if opcion == "Introduccion":
    st.title("Comenzando con :rainbow[Streamlit]")
    #Se puede cambiar el color de los titulos con :color[Palabra a afectar] funciona como en markdown

    st.header("Esto es un encabezado")
    st.subheader("Esto es un subheader")

    st.write("Hola Mundo, esta es mi primera aplicacion web usando Streamlit.")
    st.write(
        "Ejemplo de cambio de colores:"
        " :gray[gray], "
        ":red[red], "
        " :green[green], "
        ":blue[blue], "
        ":orange[orange], "
        ":violet[violet], "
        ":rainbow[rainbow]"
    )

    st.subheader("Estos son cosas interactivas",divider="rainbow")
    st.button("Esto es un boton primary", type="primary")
    st.button("Esto es un boton secondary", type="secondary")

    st.checkbox("Selecciona esta opcion")

    st.radio("Elije una de estas opciones:", ["Opcion 1", "Opcion 2", "Opcion 3"])
elif opcion == "Ahorcado":
    st.title("Ahorcado")
    