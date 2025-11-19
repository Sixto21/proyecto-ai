# Primer Chat-bot usando Modelo Gemini

*Prof. Nicolás Vassallo*

## ¿Qué es un modelo de lenguaje y cómo funciona un chatbot?

### 1- ¿Qué es un modelo de lenguaje?

- Es un tipo de inteligencia artificial que ha sido entrenado con grandes cantidades de texto.
- Aprende a predecir palabras y generar respuestas coherentes basándose en lo que se le pregunta.

**Ejemplos de Modelos:**
- GPT (OpenAI)
- Gemini (Google)
- LLaMA (Meta)

**Ejemplo simple:**
- Frase: "La tierra gira alrededor del…"
- Modelo: "sol"

### 2- ¿Qué es un LLM?

**LLM = Large Language Model**

Es un modelo de IA entrenado con cantidades enormes de texto. Puede entender y generar lenguaje de manera fluida. Tiene miles de millones de parámetros, lo que le permite entender lenguaje, contexto, intenciones, sin necesidad de reglas escritas a mano.

**Ejemplos de LLMs:**
- GPT-4 (OpenAI)
- Gemini (Google)
- LLaMA (Meta)
- Claude (Anthropic)

En nuestro chatbot usamos **Gemini 1.5 Flash**, que es un LLM optimizado por Google para responder rápido y bien.

#### ¿Cómo trabaja el LLM en el chatbot?

**Flujo:**
```
Usuario → Texto → API de Gemini → LLM analiza → Genera texto → Devuelve respuesta → Usuario
```

**Ejemplo:**
- Usuario: ¿Cuál es la capital de Japón?
- Modelo: La capital de Japón es Tokio.

### 3- ¿Qué es un prompt?

Un prompt es el texto que le damos como entrada al modelo.
- Puede ser una pregunta, una orden o una consigna.

**Ejemplo de prompts:**
- "Contame un chiste corto."
- "Traducí al inglés: 'Hola, ¿cómo estás?'"
- "Explicame qué es una base de datos relacional en lenguaje sencillo."

### 4- ¿Qué es Gemini?

- Gemini es el nombre de los modelos de lenguaje desarrollados por Google.
- Hay distintos modelos según velocidad y complejidad:
  - **gemini-1.5-flash** ➜ más rápido y liviano (ideal para chats simples)
  - **gemini-1.5-pro** ➜ más complejo, más costoso computacionalmente

### 5- ¿Qué es una API?

- Una API (Interfaz de Programación de Aplicaciones) permite comunicarnos con el modelo desde nuestro código.
- En este caso, usamos la API de Gemini para mandar preguntas y recibir respuestas.

### 6- ¿Cómo funciona un chatbot?

1. El usuario escribe un mensaje (prompt).
2. El chatbot lo envía al modelo a través de la API.
3. El modelo genera una respuesta basada en todo su entrenamiento.
4. El chatbot muestra la respuesta.

---

## Práctica: Chat con Gemini + Python

### Primero: Obtener una clave API de Gemini

- Registrarse en Google AI Studio.
- Generar y copiar la clave API.

### Seguridad: usar .env para la API KEY

#### Paso 1: .env con tu clave

`.env` (no lo subas nunca a GitHub):
```
GEMINI_API_KEY=AIzaSyD************tu_clave
```

**Crear entorno venv:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Paso 2: requirements.txt

```
google-generativeai
python-dotenv
```

**Instalación:**
```bash
pip install -r requirements.txt
```

#### Ejemplo Práctico:

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("¿Qué es la inteligencia artificial?")
print(response.text)
```

#### Paso 3: main.py

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar la clave desde .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configurar Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat()

print("🤖 Chat con Gemini - Escribí 'salir' para terminar")

while True:
    pregunta = input("🧑 Vos: ")
    
    if pregunta.lower() in ["salir", "exit", "quit"]:
        print("🤖 ¡Chau!")
        break
    
    try:
        respuesta = chat.send_message(pregunta)
        print("🤖 Bot:", respuesta.text)
    except Exception as e:
        print("❌ Error:", e)
```

### Para ejecutar

```bash
python main.py
```

### Resultado

- ✅ Chat funcional usando Gemini
- ✅ Clave protegida en .env
- ✅ Código limpio y reutilizable
