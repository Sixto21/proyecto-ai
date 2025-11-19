"""
Chatbot Básico - TP2
Un chatbot simple que responde a saludos y preguntas básicas
"""

def chatbot():
    print("¡Hola! Soy un chatbot básico. Escribe 'salir' para terminar.")
    print("-" * 50)
    
    respuestas = {
        "hola": "¡Hola! ¿Cómo estás?",
        "como estas": "¡Estoy bien, gracias! Soy un programa, así que siempre estoy bien 😊",
        "que eres": "Soy un chatbot básico creado para responder preguntas simples",
        "tu nombre": "Me llamo ChatBot v1.0",
        "ayuda": "Puedes preguntarme: hola, como estas, que eres, tu nombre, chiste",
        "chiste": "¿Por qué los programadores prefieren el modo oscuro? ¡Porque la luz atrae bugs! 🐛",
        "adios": "¡Hasta luego! Fue un gusto hablar contigo.",
        "gracias": "¡De nada! Estoy aquí para ayudarte."
    }
    
    while True:
        usuario = input("\nTú: ").lower().strip()
        
        if usuario == "salir":
            print("ChatBot: ¡Hasta pronto!")
            break
        
        # Buscar respuesta
        respuesta_encontrada = False
        for clave, respuesta in respuestas.items():
            if clave in usuario:
                print(f"ChatBot: {respuesta}")
                respuesta_encontrada = True
                break
        
        if not respuesta_encontrada:
            print("ChatBot: Lo siento, no entiendo esa pregunta. Escribe 'ayuda' para ver qué puedo hacer.")

if __name__ == "__main__":
    chatbot()
