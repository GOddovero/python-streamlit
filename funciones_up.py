import streamlit as st
from page import introduccion_ia as p
from page import introduccion_python as p

#funciones:
def cambiar_pagina(nombre_pagina):
    st.query_params.update({"page": nombre_pagina})
    return

def construir_pagina_info(titulo:str | None = "Falta colocar el titulo de esta pagina", subtitulo:str | None = "", texto_principal:str | None = ""):

    """
    Puedes usar esta funcion para crear paginas simples, pasandole un Titulo, un subtitulo y un texto principal, solamente el primero es excluyente.
    """
    st.title(titulo)
    st.subheader(subtitulo)
    st.markdown("---")
    st.write(texto_principal)
    return