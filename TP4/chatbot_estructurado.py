"""
Chatbot Estructurado - TP4
Versión mejorada con clases y POO
"""

import random

class ChatBot:
    def __init__(self, nombre="ChatBot Pro"):
        self.nombre = nombre
        self.respuestas = {
            "saludo": {
                "palabras": ["hola", "buenos dias", "buenas tardes", "hey"],
                "respuestas": ["¡Hola! ¿En qué puedo ayudarte?", "¡Hey! ¿Cómo estás?"]
            },
            "estado": {
                "palabras": ["como estas", "que tal"],
                "respuestas": ["¡Funcionando perfectamente!", "¡Genial! ¿Y tú?"]
            },
            "identidad": {
                "palabras": ["quien eres", "que eres"],
                "respuestas": [f"Soy {self.nombre}, un chatbot con POO"]
            },
            "chiste": {
                "palabras": ["chiste", "broma"],
                "respuestas": [
                    "¿Qué le dice un bit al otro? Nos vemos en el bus 😄",
                    "¿Por qué Oct 31 = Dec 25? Porque 31 en octal = 25 en decimal 🎃"
                ]
            }
        }
        self.conversaciones = []
    
    def procesar_mensaje(self, mensaje):
        mensaje = mensaje.lower().strip()
        self.conversaciones.append(("usuario", mensaje))
        
        for categoria, datos in self.respuestas.items():
            for palabra in datos["palabras"]:
                if palabra in mensaje:
                    respuesta = random.choice(datos["respuestas"])
                    self.conversaciones.append(("bot", respuesta))
                    return respuesta
        
        respuesta = "No tengo respuesta para eso. ¿Puedo ayudarte con algo más?"
        self.conversaciones.append(("bot", respuesta))
        return respuesta
    
    def iniciar(self):
        print(f"{'='*60}")
        print(f"{self.nombre} - Chatbot Estructurado")
        print(f"{'='*60}\n")
        
        while True:
            mensaje = input("Tú: ").strip()
            if mensaje.lower() == "salir":
                print(f"{self.nombre}: ¡Hasta pronto!")
                break
            
            respuesta = self.procesar_mensaje(mensaje)
            print(f"{self.nombre}: {respuesta}\n")

if __name__ == "__main__":
    bot = ChatBot("ChatBot Pro 4.0")
    bot.iniciar()
