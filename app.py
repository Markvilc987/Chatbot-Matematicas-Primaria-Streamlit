import os
import streamlit as st
from PIL import Image

# Configuración principal de la aplicación Streamlit
st.set_page_config(
    page_title="MateTutor Primaria | Retroalimentación Matemática con IA",
    page_icon="🦉",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Estilos CSS amigables para niños y niñas de primaria
st.markdown("""
<style>
    .header-box {
        background: linear-gradient(135deg, #4A90E2 0%, #50E3C2 100%);
        border-radius: 16px;
        padding: 24px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }
    .header-sub {
        font-size: 1.1rem;
        margin-top: 8px;
        opacity: 0.95;
    }
    .badge {
        display: inline-block;
        background-color: rgba(255,255,255,0.25);
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
        margin: 4px;
    }
</style>
<div class="header-box">
    <div class="header-title">🦉 MateTutor Primaria ✨</div>
    <div class="header-sub">Tu compañero inteligente para aprender matemáticas paso a paso</div>
    <div>
        <span class="badge">🍎 1° a 6° de Primaria</span>
        <span class="badge">💡 Método Socrático</span>
        <span class="badge">📸 Soporte con Fotos</span>
        <span class="badge">🎉 100% Gratuito</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 1. Gestión de API Key (Secrets en la nube o entrada manual en pruebas)
api_key = None
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
elif "GEMINI_API_KEY" in os.environ:
    api_key = os.environ["GEMINI_API_KEY"]

# Barra lateral informativa y controles
with st.sidebar:
    st.image("https://img.icons8.com/color/96/owl.png", width=70)
    st.title("Configuración y Ayuda")
    
    if not api_key:
        st.subheader("🔑 Clave de Acceso (API Key)")
        api_key = st.text_input(
            "Ingresa tu clave de Gemini:",
            type="password",
            help="Consigue tu API Key gratuita en Google AI Studio (aistudio.google.com)"
        )
        st.markdown("[👉 **Crear mi API Key gratis en Google AI Studio**](https://aistudio.google.com/app/apikey)")
        st.divider()

    # Nivel educativo del estudiante
    nivel_educativo = st.selectbox(
        "🎒 Nivel del estudiante:",
        [
            "1° y 2° Primaria (Sumas, restas y conteo básico)",
            "3° y 4° Primaria (Multiplicación, división y fracciones iniciales)",
            "5° y 6° Primaria (Fracciones, decimales, porcentajes y geometría)"
        ],
        index=1
    )

    # Subida de imagen del cuaderno o libro de trabajo
    st.subheader("📸 Sube la foto de tu cuaderno")
    uploaded_file = st.file_uploader(
        "Si no quieres escribir, tómale una foto a tu ejercicio:",
        type=["png", "jpg", "jpeg"],
        help="Sube una foto clara de tu libro o cuaderno con el problema matemático."
    )
    
    img_attachment = None
    if uploaded_file is not None:
        try:
            img_attachment = Image.open(uploaded_file)
            st.image(img_attachment, caption="Tu foto cargada", use_container_width=True)
            st.success("¡Foto lista para enviar!")
        except Exception as e:
            st.error(f"Error al abrir la imagen: {e}")

    st.divider()
    if st.button("🔄 Reiniciar conversación", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.caption("🛡️ **Privacidad y Seguridad:** Diseñado exclusivamente para fines pedagógicos escolares.")

# Si no hay API Key, detener la ejecución con mensaje instructivo
if not api_key:
    st.warning("👋 ¡Bienvenido! Por favor ingresa tu API Key gratuita de Google Gemini en la barra lateral para comenzar.")
    st.info("💡 **Consejo:** Para que tus estudiantes no tengan que ingresar la API Key, configúrala como un secreto (`GEMINI_API_KEY`) en el panel de Streamlit Community Cloud.")
    st.stop()

# 2. Configurar Google Generative AI
import google.generativeai as genai
genai.configure(api_key=api_key)

# 3. Prompt de Sistema Pedagógico
SYSTEM_INSTRUCTIONS = f"""
Eres "MateTutor", un docente virtual especializado en pedagogía de matemáticas para educación primaria (niños y niñas de 6 a 12 años).
Actualmente estás interactuando con un estudiante en el nivel: {nivel_educativo}.

TUS REGLAS Y PRINCIPIOS DE RETROALIMENTACIÓN:
1. NUNCA des la respuesta final directamente, incluso si el estudiante dice "dime la respuesta" o "dame el resultado".
2. MÉTODO SOCRÁTICO GUIADO:
   - Ayuda al niño a comprender el enunciado preguntándole: "¿De qué trata el problema?", "¿Cuáles son los datos que tenemos?" o "¿Qué nos están preguntando?".
   - Plantea solo UNA pregunta sencilla por turno.
3. CONEXIÓN VISUAL Y CONTEXTUAL:
   - Usa ejemplos concretos de la vida diaria (manzanas, canicas, caramelos, galletas, monedas, cromos, carritos de juguete).
   - Para niveles más avanzados (5°-6°), usa metáforas de pizzas o chocolates para fracciones.
4. DETECCIÓN Y CORRECCIÓN AMABLE DE ERRORES:
   - Si el estudiante responde incorrectamente, sé cálido y positivo: "¡Estuviste muy cerca! Vamos a revisar juntos: si tenías 8 caramelos y diste 3, ¿cuántos te quedaron?".
   - Nunca uses palabras como "mal", "incorrecto" o "te equivocaste". Prefiere: "¡Buen intento!", "Casi lo tienes, miremos este detalle...".
5. REFUERZO POSITIVO:
   - Celebra cada paso correcto: "¡Exacto!", "¡Brillante!", "¡Qué bien razonas! 🌟👏".
6. ESTILO DE REDACCIÓN:
   - Frases cortas, vocabulario sencillo, tono alegre y amigable.
   - Usa emojis motivadores (🚀, 💡, 🦉, 🎈, 🧩, 🏆).
   - Máximo 2 a 3 párrafos cortos por mensaje.
7. ANÁLISIS DE IMÁGENES:
   - Si el estudiante te envía una imagen de su cuaderno o libro, lee con atención el problema matemático y empieza preguntándole cuál es el primer dato que observa.
"""

# Inicializar el modelo Gemini 1.5 Flash
try:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=SYSTEM_INSTRUCTIONS
    )
except Exception as e:
    st.error(f"Error al inicializar el modelo de IA: {e}")
    st.stop()

# 4. Gestión del historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "¡Hola! 👋 Soy tu tutor de matemáticas 🦉. Cuéntame, ¿qué problema o ejercicio estás trabajando hoy? ¡Podemos resolverlo juntos paso a paso!",
            "avatar": "🦉"
        }
    ]

# Renderizar los mensajes existentes
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=msg.get("avatar", None)):
        st.markdown(msg["content"])
        if "image" in msg and msg["image"] is not None:
            st.image(msg["image"], caption="Foto enviada", width=280)

# 5. Entrada del usuario
prompt = st.chat_input("Escribe tu pregunta o respuesta aquí...")

if prompt:
    # Guardar mensaje del usuario
    user_payload = {
        "role": "user",
        "content": prompt,
        "avatar": "🧒"
    }
    if img_attachment is not None:
        user_payload["image"] = img_attachment
    
    st.session_state.messages.append(user_payload)
    with st.chat_message("user", avatar="🧒"):
        st.markdown(prompt)
        if img_attachment is not None:
            st.image(img_attachment, width=280)

    # Preparar el historial para Gemini
    chat_history = []
    for m in st.session_state.messages[:-1]:
        role = "user" if m["role"] == "user" else "model"
        chat_history.append({
            "role": role,
            "parts": [m["content"]]
        })

    # Generar respuesta con spinner
    with st.chat_message("assistant", avatar="🦉"):
        with st.spinner("MateTutor está pensando una pista para ti... 💡"):
            try:
                chat = model.start_chat(history=chat_history)
                if img_attachment is not None:
                    response = chat.send_message([prompt, img_attachment])
                else:
                    response = chat.send_message(prompt)

                reply_text = response.text
                st.markdown(reply_text)
                
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": reply_text,
                    "avatar": "🦉"
                })
            except Exception as e:
                st.error(f"Lo siento, ocurrió una pequeña pausa en la conexión: {e}")
