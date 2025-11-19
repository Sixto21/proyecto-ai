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
