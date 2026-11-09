import streamlit as st
import os

# Configuración del Pizarrón Escolar
st.set_page_config(page_title="Flujos de vida", page_icon="🌊", layout="wide")

st.title("🌊 Flujos de Vida")
st.markdown("### CBTIS 303 | Ciencias Naturales, Experimentales y Tecnología III")
st.write("Explora los conceptos fisicoquímicos que explican la dinámica de la hidrósfera y la atmósfera, y los flujos de materia y energía en los ecosistemas.")

# --- RUTAS DE IMÁGENES ---
IMAGENES = {
    "Estados_Agua": "estados_agua.png",
    "Densidad_Presion": "densidad_presion.png",
    "Temperatura_Calor": "temperatura_calor.png",
    "Tiempo_Clima": "tiempo_vs_clima.png",
    "Factores_Clima": "factores_clima.png",
    "Ecosistema": "ecosistema.png",
    "Cadena_Trofica": "cadena_trofica.png",
    "Biomasa_Productividad": "biomasa_productividad.png",
    "Ciclos_Biogeoquimicos": "ciclos_biogeoquimicos.png"
}

# --- BANCO DE PREGUNTAS ---
CUESTIONARIO = {
    "fisicoquimica": [
        {
            "id": "fis1",
            "pregunta": "¿Por qué el hielo flota en el agua líquida?",
            "opciones": [
                "Porque el hielo es menos denso que el agua líquida",
                "Porque el hielo es más denso que el agua líquida",
                "Porque el hielo está más caliente que el agua"
            ],
            "correcta": "Porque el hielo es menos denso que el agua líquida",
            "pista": "Revisa la subpestaña 'Densidad y Presión'."
        },
        {
            "id": "fis2",
            "pregunta": "¿Qué ocurre con la presión atmosférica a medida que subimos una montaña?",
            "opciones": [
                "Disminuye, porque hay menos aire encima",
                "Aumenta, porque estamos más cerca del Sol",
                "Se mantiene igual a cualquier altura"
            ],
            "correcta": "Disminuye, porque hay menos aire encima",
            "pista": "Revisa la subpestaña 'Densidad y Presión'."
        },
        {
            "id": "fis3",
            "pregunta": "¿Qué cambio de estado ocurre cuando el vapor de agua se convierte en gotas líquidas?",
            "opciones": [
                "Condensación",
                "Evaporación",
                "Sublimación"
            ],
            "correcta": "Condensación",
            "pista": "Revisa la subpestaña 'Estados de Agregación'."
        },
        {
            "id": "fis4",
            "pregunta": "¿Cuál es la diferencia entre temperatura y calor?",
            "opciones": [
                "La temperatura mide la energía cinética promedio; el calor es la transferencia de energía",
                "Son exactamente lo mismo",
                "El calor se mide en grados y la temperatura en joules"
            ],
            "correcta": "La temperatura mide la energía cinética promedio; el calor es la transferencia de energía",
            "pista": "Revisa la subpestaña 'Temperatura y Calor'."
        }
    ],
    "clima": [
        {
            "id": "cli1",
            "pregunta": "¿Cuál es la diferencia entre tiempo atmosférico y clima?",
            "opciones": [
                "El tiempo es a corto plazo; el clima es el promedio a largo plazo (≥30 años)",
                "El tiempo es a largo plazo; el clima es momentáneo",
                "No hay diferencia, son sinónimos"
            ],
            "correcta": "El tiempo es a corto plazo; el clima es el promedio a largo plazo (≥30 años)",
            "pista": "Revisa la subpestaña 'Tiempo vs Clima'."
        },
        {
            "id": "cli2",
            "pregunta": "¿Qué factor del clima explica por qué hace más frío en las montañas altas?",
            "opciones": [
                "La altitud",
                "La latitud",
                "Las corrientes marinas"
            ],
            "correcta": "La altitud",
            "pista": "Revisa la subpestaña 'Factores que Modifican el Clima'."
        },
        {
            "id": "cli3",
            "pregunta": "¿Cuántos años se necesitan, como mínimo, para definir el clima de un lugar?",
            "opciones": [
                "30 años",
                "1 año",
                "100 años"
            ],
            "correcta": "30 años",
            "pista": "Revisa la subpestaña 'Tiempo vs Clima'."
        },
        {
            "id": "cli4",
            "pregunta": "¿Qué factor del clima explica que las zonas cercanas al ecuador sean más cálidas?",
            "opciones": [
                "La latitud",
                "La altitud",
                "El relieve"
            ],
            "correcta": "La latitud",
            "pista": "Revisa la subpestaña 'Factores que Modifican el Clima'."
        }
    ],
    "flujos": [
        {
            "id": "flu1",
            "pregunta": "¿Qué son los componentes bióticos y abióticos de un ecosistema?",
            "opciones": [
                "Bióticos: seres vivos; abióticos: factores físicos y químicos",
                "Bióticos: minerales; abióticos: plantas",
                "Bióticos: agua y aire; abióticos: animales"
            ],
            "correcta": "Bióticos: seres vivos; abióticos: factores físicos y químicos",
            "pista": "Revisa la subpestaña 'Ecosistema y Biodiversidad'."
        },
        {
            "id": "flu2",
            "pregunta": "¿Cuál es el orden correcto de una cadena trófica?",
            "opciones": [
                "Productores → consumidores primarios → consumidores secundarios → descomponedores",
                "Descomponedores → productores → consumidores",
                "Consumidores → productores → descomponedores"
            ],
            "correcta": "Productores → consumidores primarios → consumidores secundarios → descomponedores",
            "pista": "Revisa la subpestaña 'Cadena Trófica y Eficiencia Ecológica'."
        },
        {
            "id": "flu3",
            "pregunta": "¿Qué porcentaje de energía se transfiere aproximadamente de un nivel trófico al siguiente?",
            "opciones": [
                "10%",
                "50%",
                "90%"
            ],
            "correcta": "10%",
            "pista": "Revisa la subpestaña 'Cadena Trófica y Eficiencia Ecológica'."
        },
        {
            "id": "flu4",
            "pregunta": "¿Por qué el ciclo del fósforo es especial entre los ciclos biogeoquímicos?",
            "opciones": [
                "Porque no tiene fase gaseosa y solo se libera por erosión de rocas",
                "Porque ocurre solo en la atmósfera",
                "Porque no participa en la vida de los seres vivos"
            ],
            "correcta": "Porque no tiene fase gaseosa y solo se libera por erosión de rocas",
            "pista": "Revisa la subpestaña 'Ciclos Biogeoquímicos'."
        },
        {
            "id": "flu5",
            "pregunta": "¿Qué es el equilibrio ecológico y qué lo altera?",
            "opciones": [
                "Es un estado dinámico de estabilidad; lo alteran la contaminación y la deforestación",
                "Es un estado fijo que nunca cambia",
                "Es la cantidad de agua en un ecosistema"
            ],
            "correcta": "Es un estado dinámico de estabilidad; lo alteran la contaminación y la deforestación",
            "pista": "Revisa la subpestaña 'Biomasa, Productividad y Equilibrio Ecológico'."
        }
    ]
}

# --- FUNCIÓN PARA MOSTRAR IMÁGENES ---
def mostrar_imagen(nombre_archivo, texto_alternativo):
    if os.path.exists(nombre_archivo):
        st.image(nombre_archivo, caption=texto_alternativo, use_container_width=True)
    else:
        st.warning(f"⚠️ Guarda una imagen llamada '{nombre_archivo}' en tu carpeta para verla aquí.")

# --- PESTAÑAS PRINCIPALES ---
tab_fisico, tab_clima, tab_flujos = st.tabs([
    "🌡️ Fisicoquímica del Agua y el Aire",
    "☀️ Clima y Tiempo Atmosférico",
    "🔄 Flujos de Materia y Energía"
])

# ============================================================
# PESTAÑA 1: FISICOQUÍMICA DEL AGUA Y EL AIRE
# ============================================================
with tab_fisico:
    st.header("🌡️ Fisicoquímica del Agua y el Aire")

    sub1, sub2, sub3 = st.tabs([
        "💧 Estados de Agregación",
        "⚖️ Densidad y Presión",
        "🌡️ Temperatura y Calor"
    ])

    # --- Subpestaña 1: Estados de Agregación ---
    with sub1:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Estados_Agua"], "Estados de agregación del agua y sus cambios de estado.")
        with col2:
            st.success("### 💧 Estados de Agregación del Agua")
            st.markdown("""
            El agua puede encontrarse en tres estados:
            - **Sólido:** Hielo (estructura cristalina ordenada).
            - **Líquido:** Agua (partículas con libertad de movimiento).
            - **Gaseoso:** Vapor de agua (partículas dispersas y rápidas).
            """)
            st.info("### 🔄 Cambios de Estado")
            st.markdown("""
            - **Fusión:** Sólido → Líquido (derretimiento).
            - **Solidificación:** Líquido → Sólido (congelación).
            - **Evaporación:** Líquido → Gas (absorbe energía).
            - **Condensación:** Gas → Líquido (libera energía).
            - **Sublimación:** Sólido → Gas (sin pasar por líquido).
            """)
            st.warning("### 🌍 Aplicación en la Tierra")
            st.markdown("""
            - La **condensación** forma las nubes.
            - La **evaporación** ocurre en océanos y ríos por la energía solar.
            - La **sublimación** ocurre en glaciares y nieve expuestos al sol.
            """)

    # --- Subpestaña 2: Densidad y Presión ---
    with sub2:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Densidad_Presion"], "Comparación de densidad y variación de la presión atmosférica con la altura.")
        with col2:
            st.success("### ⚖️ Densidad")
            st.markdown("""
            La **densidad** es la cantidad de masa por unidad de volumen.
            - **Agua líquida:** ~1 g/cm³.
            - **Hielo:** ~0.92 g/cm³ → **por eso flota**.
            - **Agua salada:** ~1.025 g/cm³ (más densa que la dulce).
            """)
            st.info("### 🌬️ Presión Atmosférica")
            st.markdown("""
            Es la fuerza que ejerce el peso del aire sobre la superficie.
            - **A nivel del mar:** ~1013 hPa.
            - **Disminuye con la altura:** a mayor altitud, menos aire encima.
            - **A 5,500 m:** ~500 hPa (la mitad).
            """)
            st.warning("### 🌍 Aplicación en la Tierra")
            st.markdown("""
            - El hielo flota y aísla el agua debajo, permitiendo vida en lagos congelados.
            - La presión baja en altura explica el mal de montaña.
            - Las diferencias de presión generan los vientos.
            """)

    # --- Subpestaña 3: Temperatura y Calor ---
    with sub3:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Temperatura_Calor"], "Diferencia entre temperatura y calor, y gradientes térmicos.")
        with col2:
            st.success("### 🌡️ Temperatura vs Calor")
            st.markdown("""
            - **Temperatura:** Medida de la energía cinética promedio de las partículas (°C, K).
            - **Calor:** Transferencia de energía térmica de un cuerpo a otro (Joules).
            """)
            st.info("### 📊 Gradientes Térmicos")
            st.markdown("""
            - **Atmósfera:** La temperatura cambia con la altura (Troposfera: disminuye; Estratosfera: aumenta).
            - **Océano:** La temperatura disminuye con la profundidad.
            - **Suelo:** Aumenta con la profundidad (gradiente geotérmico).
            """)
            st.warning("### 🌍 Aplicación en la Tierra")
            st.markdown("""
            - El calor latente de evaporación enfría la superficie (sudor, lluvia).
            - Los gradientes térmicos generan corrientes de convección (vientos, corrientes marinas).
            """)

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre Fisicoquímica"):
        for q in CUESTIONARIO["fisicoquimica"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# ============================================================
# PESTAÑA 2: CLIMA Y TIEMPO ATMOSFÉRICO
# ============================================================
with tab_clima:
    st.header("☀️ Clima y Tiempo Atmosférico")

    sub1, sub2 = st.tabs([
        "⏱️ Tiempo vs Clima",
        "🌍 Factores que Modifican el Clima"
    ])

    # --- Subpestaña 1: Tiempo vs Clima ---
    with sub1:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Tiempo_Clima"], "Comparación entre tiempo atmosférico y clima.")
        with col2:
            st.success("### ⏱️ Tiempo Atmosférico")
            st.markdown("""
            Es el **estado de la atmósfera en un momento y lugar determinados**.
            - Duración: horas o días.
            - Ejemplo: "Hoy hace calor y hay nubes en la tarde".
            """)
            st.info("### 📅 Clima")
            st.markdown("""
            Es el **promedio de las condiciones atmosféricas** durante al menos **30 años**.
            - Duración: décadas.
            - Ejemplo: "El clima de esta región es tropical húmedo".
            """)
            st.warning("### 🌡️ Cambio Climático")
            st.markdown("""
            Es una alteración del **clima a largo plazo**, no del tiempo de un día.
            Se debe al aumento de gases de efecto invernadero.
            """)

    # --- Subpestaña 2: Factores que Modifican el Clima ---
    with sub2:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Factores_Clima"], "Factores que modifican el clima: latitud, altitud, corrientes marinas y relieve.")
        with col2:
            st.success("### 🌍 Factores del Clima")
            st.markdown("""
            - **Latitud:** Cerca del ecuador hay más calor; cerca de los polos, más frío.
            - **Altitud:** A mayor altura, menor temperatura (≈ -6 °C por km).
            - **Corrientes marinas:** Modera la temperatura de las costas (ej. Corriente del Golfo).
            - **Relieve:** Las montañas actúan como barreras (efecto Föhn, sombra de lluvia).
            """)
            st.info("### 🗺️ Ejemplos")
            st.markdown("""
            - **Ecuador:** Clima cálido todo el año (latitud baja).
            - **Ciudad de México:** Clima templado por su altitud (~2,240 m).
            - **Europa occidental:** Clima suave por la Corriente del Golfo.
            """)

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre Clima y Tiempo"):
        for q in CUESTIONARIO["clima"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# ============================================================
# PESTAÑA 3: FLUJOS DE MATERIA Y ENERGÍA
# ============================================================
with tab_flujos:
    st.header("🔄 Flujos de Materia y Energía en los Ecosistemas")

    sub1, sub2, sub3, sub4 = st.tabs([
        "🌿 Ecosistema y Biodiversidad",
        "🔗 Cadena Trófica y Eficiencia",
        "📊 Biomasa y Equilibrio",
        "♻️ Ciclos Biogeoquímicos"
    ])

    # --- Subpestaña 1: Ecosistema y Biodiversidad ---
    with sub1:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Ecosistema"], "Componentes bióticos y abióticos de un ecosistema.")
        with col2:
            st.success("### 🌿 Ecosistema")
            st.markdown("""
            Es el conjunto de **seres vivos** y su **ambiente físico** que interactúan.
            - **Bióticos:** Plantas, animales, hongos, bacterias.
            - **Abióticos:** Agua, aire, suelo, luz, temperatura.
            """)
            st.info("### 🦋 Biodiversidad")
            st.markdown("""
            Es la **variedad de especies** en un ecosistema.
            - Incluye diversidad genética, de especies y de ecosistemas.
            - México es un país megadiverso (2° lugar mundial en reptiles).
            """)
            st.warning("### 🔗 Interacciones")
            st.markdown("""
            Los seres vivos modifican su ambiente y viceversa.
            Ejemplo: las raíces rompen rocas (biodeterioro) y crean suelo.
            """)

    # --- Subpestaña 2: Cadena Trófica y Eficiencia ---
    with sub2:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Cadena_Trofica"], "Pirámide trófica y flujo de energía entre niveles.")
        with col2:
            st.success("### 🔗 Cadena Trófica")
            st.markdown("""
            Es la secuencia de transferencia de energía entre organismos:
            - **Productores:** Plantas y algas (fotosíntesis).
            - **Consumidores primarios:** Herbívoros.
            - **Consumidores secundarios:** Carnívoros.
            - **Descomponedores:** Hongos y bacterias.
            """)
            st.info("### ⚡ Eficiencia Ecológica")
            st.markdown("""
            Solo el **10%** de la energía pasa de un nivel al siguiente.
            El 90% restante se pierde como calor (respiración, metabolismo).
            Por eso las pirámides tróficas tienen forma de pirámide.
            """)
            st.warning("### 📉 Implicación")
            st.markdown("""
            Se necesitan **10,000 kg de plantas** para producir **1 kg de carnívoro**.
            Por eso las dietas basadas en vegetales son más eficientes.
            """)

    # --- Subpestaña 3: Biomasa y Equilibrio ---
    with sub3:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Biomasa_Productividad"], "Biomasa, productividad primaria y equilibrio ecológico.")
        with col2:
            st.success("### 📊 Biomasa")
            st.markdown("""
            Es la **cantidad total de materia orgánica viva** en un ecosistema.
            - Se mide en g/m² o kg/ha.
            - La mayor biomasa está en bosques y océanos.
            """)
            st.info("### 🌱 Productividad Primaria")
            st.markdown("""
            Es la **velocidad** a la que los productores generan nueva biomasa.
            - **Neta:** Lo que queda después de la respiración.
            - **Bruta:** Total producido por fotosíntesis.
            """)
            st.warning("### ⚖️ Equilibrio Ecológico")
            st.markdown("""
            Es un estado **dinámico** de estabilidad entre poblaciones y flujos.
            - Se altera por contaminación, deforestación, especies invasoras.
            - Sin equilibrio, el ecosistema colapsa.
            """)

    # --- Subpestaña 4: Ciclos Biogeoquímicos ---
    with sub4:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["Ciclos_Biogeoquimicos"], "Ciclos biogeoquímicos del carbono, nitrógeno y fósforo.")
        with col2:
            st.success("### ♻️ Ciclos Biogeoquímicos")
            st.markdown("""
            Son los **recorridos circulares** de los elementos entre las esferas terrestres.
            - **Carbono:** Atmósfera ↔ Biosfera ↔ Litosfera ↔ Hidrosfera.
            - **Nitrógeno:** Atmósfera → Suelo → Biosfera → Atmósfera.
            - **Fósforo:** Litosfera → Biosfera → Litosfera.
            """)
            st.info("### 🔬 El Caso del Fósforo")
            st.markdown("""
            Es el **único ciclo sin fase gaseosa**.
            Solo se libera de la Litosfera a la Biosfera por **erosión de rocas**.
            Por eso es un nutriente limitante en muchos ecosistemas.
            """)
            st.warning("### 🌍 Importancia")
            st.markdown("""
            - El carbono regula el clima (efecto invernadero).
            - El nitrógeno forma proteínas y ADN.
            - El fósforo forma ATP y huesos.
            """)

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre Flujos y Ciclos"):
        for q in CUESTIONARIO["flujos"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")