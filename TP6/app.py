"""
Aplicación Flask - TP6
Frontend web con Flask para chatbot
"""

from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)

class ChatBotWeb:
    def __init__(self):
        self.respuestas = {
            "hola": ["¡Hola! ¿Cómo estás?", "¡Hey! Bienvenido/a"],
            "como estas": ["¡Estoy bien!", "¡Funcionando perfectamente!"],
            "que eres": ["Soy un chatbot web con Flask"],
            "ayuda": ["Puedo responder preguntas básicas"],
            "hora": [f"Hora: {datetime.now().strftime('%H:%M')}"],
            "chiste": [
                "¿Por qué los programadores prefieren el modo oscuro? ¡Luz atrae bugs! 🐛",
                "¿Qué le dice un bit al otro? Nos vemos en el bus 😄"
            ]
        }
    
    def responder(self, mensaje):
        mensaje = mensaje.lower().strip()
        for clave, respuestas in self.respuestas.items():
            if clave in mensaje:
                return random.choice(respuestas)
        return "No tengo respuesta para eso. ¿Algo más?"

bot = ChatBotWeb()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    mensaje = data.get('mensaje', '')
    respuesta = bot.responder(mensaje)
    return jsonify({
        'respuesta': respuesta,
        'timestamp': datetime.now().strftime('%H:%M:%S')
    })

if __name__ == '__main__':
    print("🚀 Servidor Flask: http://localhost:5000")
    app.run(debug=True, port=5000)
