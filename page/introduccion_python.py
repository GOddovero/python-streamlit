import funciones_up as fup

def mostrar_pagina_python():
    fup.st.title("Introducción a la Python")
    fup.st.write("Aquí aprenderás los conceptos básicos y aplicaciones de la IA...")
    if fup.st.button("Volver al Inicio"):
        fup.cambiar_pagina("up_index")