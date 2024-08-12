import funciones_up as fup



#menu_principal = st.sidebar.selectbox("Elije un curso", ["Inteligencia Artificial", "Python"])
#selector de cursos:
fup.st.sidebar.image("img/logo_up.png", "Universidad Popular", 200)
curso_seleccionado = fup.st.sidebar.selectbox("Menú de Cursos", ["Universidad Popular","Inteligencia Artificial", "Python", "Gerontologia", "Electricidad"])

if curso_seleccionado == "Universidad Popular":
   fup.construir_pagina_info("Universidad Popular","General Levalle-Cordoba", "El Programa Universidades Populares de la Secretaría de Extensión de la Universidad Nacional de Córdoba tiene como finalidad principal rescatar y poner en valor la valiosa experiencia de la figura de las universidades populares, instituciones de larga historia y recorrido en el mundo y también en nuestro país.Las Universidades Populares son una conjunción lograda de manera muy exitosa, de las antiguas escuelas de arte y oficios, de las bibliotecas populares, las asociaciones culturales locales, los clubes deportivos y otras instituciones de las fuerzas vivas de pueblos y ciudades, que le dan a estas instituciones un carácter universal y participativo en la formación cultural, democrática y para el empleo de sus adherentes.")
if curso_seleccionado == "Inteligencia Artificial":
   fup.construir_pagina_info(curso_seleccionado, texto_principal="La Inteligencia Artificial (IA) es un campo fascinante que ha capturado la imaginación de científicos, ingenieros y la sociedad en general. En el contexto de la ingeniería de prompts, comprender qué es la IA y cómo se relaciona con la inteligencia natural es fundamental para desarrollar sistemas de conversación eficaces y comprender su potencial y sus limitaciones.")
if curso_seleccionado == "Python":
    fup.construir_pagina_info(curso_seleccionado, texto_principal="Python es un lenguaje de programación versátil y poderoso, ampliamente utilizado en el desarrollo web, la ciencia de datos, y la automatización. Este curso te guiará a través de los conceptos fundamentales de Python, incluyendo su sintaxis, estructuras de datos, y librerías más populares. Ideal para principiantes y desarrolladores que desean expandir sus habilidades en programación.")
    fup.st.sidebar.button("Volver al Inicio")

if curso_seleccionado == "Gerontologia":
    fup.construir_pagina_info(curso_seleccionado, texto_principal="La Gerontología es el estudio del envejecimiento y sus efectos en las personas. Este curso explora cómo el envejecimiento afecta la salud física y mental, así como las estrategias para mejorar la calidad de vida en la tercera edad. Aprende sobre los cambios biológicos, psicológicos y sociales asociados con el envejecimiento y cómo proporcionar apoyo efectivo a los adultos mayores.")

if curso_seleccionado == "Electricidad":
    fup.construir_pagina_info(curso_seleccionado, texto_principal="El curso de Electricidad cubre los principios fundamentales de la electricidad y su aplicación en instalaciones eléctricas. Aprenderás sobre circuitos eléctricos, componentes, y las mejores prácticas para garantizar instalaciones seguras y eficientes. Ideal para aquellos que desean adquirir conocimientos básicos y avanzados en electricidad y electrónica.")
