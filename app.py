import streamlit as st
import os

# Configuración del Pizarrón Escolar
st.set_page_config(page_title="Flujos de vida", page_icon="🌊", layout="wide")

st.title("🌊 Flujos de Vida")
st.markdown("### CBTIS 303 | Ciencias Naturales, Experimentales y Tecnología III")
st.write("Explora los conceptos fisicoquímicos que explican la dinámica de la hidrósfera y la atmósfera, y los flujos de materia y energía en los ecosistemas.")

# --- RUTAS DE IMÁGENES ---
# Regla aplicada: Palabra_Palabra, Palabra_Palabra2, Palabra_Palabra3
IMAGENES = {
    # Pestaña 1: Fisicoquímica
    "estados_agua": "estados_agua.png",
    "estados_agua2": "estados_agua2.png",
    "densidad_presion": "densidad_presion.jpg",
    "temperatura_calor": "temperatura_calor.png",
    "gradiente_atmosfera": "gradiente_atmosfera.png",
    "gradiente_hidrosfera": "gradiente_hidrosfera.png",
    "gradiente_litosfera": "gradiente_litosfera.png",
    
    # Pestaña 2: Clima
    "tiempo_clima": "tiempo_clima.png",
    "factores_clima": "factores_clima.png",
    
    # Pestaña 3: Flujos
    "ecosistema": "ecosistema.png",
    "cadena_trofica": "cadena_trofica.png",
    "biomasa_productividad": "biomasa_productividad.png",
    "biomasa_productividad2": "biomasa_productividad2.png",
    "biomasa_productividad3": "biomasa_productividad3.png",
    "ciclo_carbono": "ciclo_carbono.png",
    "ciclo_nitrogeno": "ciclo_nitrogeno.png",
    "ciclo_fosforo": "ciclo_fosforo.png"
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
            mostrar_imagen(IMAGENES["estados_agua"], "Estados de agregación y cambios de estado del agua.")
            st.write("") 
            mostrar_imagen(IMAGENES["estados_agua2"], "Ejemplos de estos estados en la Tierra (nubes, hielo, vapor).")
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
            mostrar_imagen(IMAGENES["densidad_presion"], "Comparación de densidad y variación de la presión atmosférica con la altura.")
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
            
            *Observa la imagen: los puntos azules representan las moléculas de aire. A mayor altura, están más separadas, lo que significa menor densidad y menor presión.*
              
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
            mostrar_imagen(IMAGENES["temperatura_calor"], "Diferencia conceptual entre temperatura y calor.")
            st.write("") 
            mostrar_imagen(IMAGENES["gradiente_atmosfera"], "Gradiente térmico en la Atmósfera.")
            st.write("") 
            mostrar_imagen(IMAGENES["gradiente_hidrosfera"], "Gradiente térmico en el Océano (Termoclina).")
            st.write("") 
            mostrar_imagen(IMAGENES["gradiente_litosfera"], "Gradiente geotérmico en el Suelo.")
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
            mostrar_imagen(IMAGENES["tiempo_clima"], "Comparación entre tiempo atmosférico y clima.")
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
            mostrar_imagen(IMAGENES["factores_clima"], "Factores que modifican el clima: latitud, altitud, corrientes marinas, relieve, vientos y distancia al mar.")
        with col2:
            st.success("### 🌍 Factores del Clima")
            st.markdown("""
            - **Latitud:** Cerca del ecuador hay más calor; cerca de los polos, más frío.
            - **Altitud:** A mayor altura, menor temperatura (≈ -6 °C por km).
            - **Corrientes marinas:** Modera la temperatura de las costas (ej. Corriente del Golfo).
            - **Relieve:** Las montañas actúan como barreras (efecto Föhn, sombra de lluvia).
            - **Vientos predominantes:** Determinan qué masa de aire (húmedo o seco) llega a una zona.
            - **Distancia al mar:** El agua tarda más en calentarse/enfriarse que la tierra, moderando el clima costero.
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
            mostrar_imagen(IMAGENES["ecosistema"], "Componentes bióticos y abióticos de un ecosistema.")
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
            mostrar_imagen(IMAGENES["cadena_trofica"], "Pirámide trófica y flujo de energía entre niveles.")
        with col2:
            st.success("### 🔗 Cadena Trófica")
            st.markdown("""
            Es la secuencia de transferencia de energía entre organismos:
            - **Productores:** Plantas y algas (fotosíntesis).
            - **Consumidores primarios:** Herbívoros.
            - **Consumidores secundarios:** Carnívoros.
            - **Descomponedores:** Hongos y bacterias.
            """)
            st.info("### ⚡ Eficiencia Ecológica (La Ley del 10%)")
            st.markdown("""
            Solo el **10%** de la energía pasa de un nivel al siguiente. 
            ¿A dónde se va el otro 90%?
            - **Respiración y calor:** El animal gasta energía para moverse y mantenerse caliente.
            - **Excreción:** Lo que el animal no digiere (heces y orina).
            - **Partes no consumidas:** Huesos, pelaje o raíces.
            """)
            st.warning("### 📉 Implicación")
            st.markdown("""
            Se necesitan **10,000 kg de plantas** para producir **1 kg de carnívoro**.
            Por eso las pirámides tróficas son más anchas en la base.
            """)

    # --- Subpestaña 3: Biomasa y Equilibrio ---
    with sub3:
        col1, col2 = st.columns([1.2, 1])
        with col1:
            mostrar_imagen(IMAGENES["biomasa_productividad"], "Distribución de la biomasa animal en el planeta.")
            st.write("") 
            mostrar_imagen(IMAGENES["biomasa_productividad2"], "Distribución de la biomasa vegetal (las plantas dominan).")
            st.write("") 
            mostrar_imagen(IMAGENES["biomasa_productividad3"], "Gráfica científica comparativa de biomasa marina y terrestre.")
        with col2:
            st.success("### 📊 Biomasa")
            st.markdown("""
            Es la **cantidad total de materia orgánica viva** en un ecosistema (el 'inventario').
            - Se mide en Gigatoneladas de Carbono (GtC).
            - La mayor biomasa está en las plantas terrestres y en los océanos.
            """)
            st.info("### 🌱 Productividad Primaria")
            st.markdown("""
            Es la **velocidad** a la que los productores generan nueva biomasa (el 'salario').
            - **Neta:** Lo que queda después de la respiración de la planta.
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
            mostrar_imagen(IMAGENES["ciclo_carbono"], "Ciclo biogeoquímico del Carbono.")
            st.write("") 
            mostrar_imagen(IMAGENES["ciclo_nitrogeno"], "Ciclo biogeoquímico del Nitrógeno.")
            st.write("") 
            mostrar_imagen(IMAGENES["ciclo_fosforo"], "Ciclo biogeoquímico del Fósforo (sin fase gaseosa).")
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