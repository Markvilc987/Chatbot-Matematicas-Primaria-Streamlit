# 🦉 MateTutor Primaria: Chatbot Educativo para Retroalimentación Matemática con IA

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB.svg?logo=python&logoColor=white)](https://python.org)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-4285F4.svg?logo=google&logoColor=white)](https://aistudio.google.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aplicación web interactiva desarrollada en **Streamlit** y potenciada por **Google Gemini 1.5 Flash**, diseñada específicamente como tutor pedagógico virtual para brindar **retroalimentación formativa y guiada** en matemáticas a estudiantes de **educación primaria (1° a 6° grado)**.

---

## 🌟 Características Pedagógicas Principales

* 💡 **Método Socrático Puro:** El chatbot **nunca da la solución directa**. Plantea preguntas guía, desglosa el problema en pasos manejables y ayuda al niño a reflexionar para llegar a la respuesta por sí mismo.
* 🍎 **Analogías Concretas y Cotidianas:** Modela problemas abstractos utilizando objetos de la vida diaria (manzanas, canicas, caramelos, galletas, monedas y juguetes).
* 📸 **Soporte Multimodal (Fotos de Cuadernos):** Los estudiantes pueden subir fotos de su libro o cuaderno con su celular; la IA reconoce el texto e imágenes del ejercicio y lo analiza en segundos.
* 🎒 **Adaptación por Ciclos de Primaria:**
  * **1° y 2° de Primaria:** Sumas, restas, conteo y números hasta el 100.
  * **3° y 4° de Primaria:** Multiplicación, división, tablas y fracciones iniciales.
  * **5° y 6° de Primaria:** Fracciones complejas, números decimales, geometría básica y porcentajes.
* 🛡️ **Refuerzo Positivo Continuo:** Lenguaje empático, libre de juicios punitivos y con motivación constante mediante emojis y felicitaciones.

---

## 🚀 Despliegue Gratuito en la Nube (Streamlit Community Cloud)

Este proyecto está listo para ser desplegado en servidores públicos **100% gratuitos** en menos de 3 minutos:

1. **Obtener la clave de Google Gemini (Gratis):**
   * Ingresa a [Google AI Studio](https://aistudio.google.com/app/apikey) y genera tu clave gratuita (permite hasta 1,500 consultas diarias sin ingresar tarjeta de crédito).
2. **Subir a GitHub:**
   * Haz un fork o sube este repositorio a tu cuenta de GitHub.
3. **Conectar a Streamlit Cloud:**
   * Entra a [share.streamlit.io](https://share.streamlit.io/) e inicia sesión con GitHub.
   * Haz clic en **"New app"**, selecciona este repositorio, la rama `main` y el archivo `app.py`.
4. **Configurar el Secreto de la API:**
   * En la configuración avanzada (**Advanced settings -> Secrets**), agrega tu clave:
     ```toml
     GEMINI_API_KEY = "tu_clave_de_google_ai_studio"
     ```
   * Haz clic en **Deploy!** y obtendrás tu URL pública permanente (`https://tu-repo.streamlit.app`).

---

## 💻 Ejecución Local

Si deseas probar la aplicación en tu computadora:

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/Chatbot-Matematicas-Primaria-Streamlit.git
cd Chatbot-Matematicas-Primaria-Streamlit

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar API Key
export GEMINI_API_KEY="tu_clave_aqui"

# 4. Iniciar la aplicación
streamlit run app.py
```

---

## 📁 Estructura del Repositorio

```
.
├── app.py                      # Aplicación principal de Streamlit con System Prompt pedagógico
├── requirements.txt            # Dependencias del proyecto
├── .gitignore                  # Exclusión de archivos temporales y claves secretas
├── .streamlit/
│   ├── config.toml             # Configuración visual y tema accesible para niños
│   └── secrets.toml.example    # Plantilla de ejemplo para variables de entorno
└── README.md                   # Documentación completa y guía de despliegue
```

---

## 📜 Licencia

Distribuido bajo la licencia **MIT**. Libre para uso educativo, escolar, investigativo y comunitario.
