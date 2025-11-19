"""
Chatbot Mejorado con IA - TP5
Versión avanzada con NLP básico y análisis
"""

import re
from datetime import datetime
import random

class ChatBotIA:
    def __init__(self, nombre="ChatBot IA"):
        self.nombre = nombre
        self.historial = []
        self.usuario_nombre = None
        
        self.conocimiento = {
            "python": "Python es un lenguaje de programación de alto nivel.",
            "ia": "La IA busca crear sistemas con inteligencia humana.",
            "machine learning": "ML permite a las computadoras aprender de datos.",
            "git": "Git es un sistema de control de versiones."
        }
    
    def extraer_nombre(self, mensaje):
        patrones = [r"me llamo (.+)", r"mi nombre es (.+)", r"soy (.+)"]
        for patron in patrones:
            match = re.search(patron, mensaje.lower())
            if match:
                return match.group(1).strip().title()
        return None
    
    def buscar_conocimiento(self, mensaje):
        for tema, info in self.conocimiento.items():
            if tema in mensaje.lower():
                return info
        return None
    
    def analizar_sentimiento(self, mensaje):
        positivas = ["bien", "genial", "feliz", "perfecto"]
        negativas = ["mal", "triste", "horrible"]
        
        mensaje_lower = mensaje.lower()
        if any(p in mensaje_lower for p in positivas):
            return "positivo"
        elif any(n in mensaje_lower for n in negativas):
            return "negativo"
        return "neutral"
    
    def procesar_mensaje(self, mensaje):
        self.historial.append(("usuario", mensaje))
        mensaje_lower = mensaje.lower().strip()
        
        # Detectar nombre
        if not self.usuario_nombre:
            nombre = self.extraer_nombre(mensaje)
            if nombre:
                self.usuario_nombre = nombre
                return f"¡Encantado, {self.usuario_nombre}!"
        
        # Saludos
        if any(s in mensaje_lower for s in ["hola", "hey"]):
            return f"¡Hola{', ' + self.usuario_nombre if self.usuario_nombre else ''}!"
        
        # Conocimiento
        conocimiento = self.buscar_conocimiento(mensaje)
        if conocimiento:
            return conocimiento
        
        # Sentimiento
        sentimiento = self.analizar_sentimiento(mensaje)
        if sentimiento == "positivo":
            return "¡Me alegra tu actitud positiva!"
        elif sentimiento == "negativo":
            return "Lamento eso. ¿Puedo ayudarte?"
        
        return "Interesante. No tengo info sobre eso, pero estoy aquí para ayudar."
    
    def iniciar(self):
        print(f"{'='*70}")
        print(f"{self.nombre} - Chatbot con IA")
        print(f"{'='*70}\n")
        
        while True:
            mensaje = input("Tú: ").strip()
            if mensaje.lower() == "salir":
                print(f"{self.nombre}: ¡Hasta pronto!")
                break
            
            respuesta = self.procesar_mensaje(mensaje)
            print(f"{self.nombre}: {respuesta}\n")

if __name__ == "__main__":
    bot = ChatBotIA("ChatBot IA 5.0")
    bot.iniciar()
