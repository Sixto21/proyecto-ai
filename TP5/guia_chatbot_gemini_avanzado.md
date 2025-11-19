# Clase: Chatbot con Gemini II

*Prof. Nicolás Vassallo*

## 1. Recordemos: ¿Qué es un chatbot con LLM?

- Un modelo de lenguaje (LLM) es un sistema de IA entrenado con muchísimos textos, capaz de entender y generar respuestas coherentes.
- **Ejemplos:** GPT (OpenAI), Gemini (Google), LLaMA (Meta), Claude (Anthropic).
- Un chatbot funciona así: **Usuario → prompt → API → LLM procesa → genera respuesta → Usuario.**

## 2. ¿Por qué necesitamos mejorar el chatbot?

El código inicial funcionaba, pero era muy básico. 

**Problemas:**
- No tenía memoria de la conversación.
- No podíamos cambiar el comportamiento del bot (profesor, traductor, etc.).
- No manejaba errores (si la API fallaba, se rompía).

## 3. Buenas prácticas que vamos a aplicar

1. **Configurar el proyecto con .env** → seguridad: la API Key nunca debe estar en el código.
2. **Separar responsabilidades en módulos** (config, memory, llm_client, etc.).
3. **Agregar memoria** → el bot recuerda los últimos mensajes.
4. **Roles** → podemos decirle "actuá como profesor" o "actúa como programador".
5. **Manejo de errores con reintentos** → más robusto.

## 4. Estructura del proyecto

```
chatbot-gemini/
├─ .env                 # clave API y configuraciones
├─ requirements.txt     # librerías necesarias
├─ main.py             # interfaz de consola
├─ config.py           # configuración
├─ llm_client.py       # conexión con Gemini
├─ memory.py           # memoria de la conversación
├─ roles.py            # modos de uso del bot
├─ prompts.py          # construcción de prompts
└─ chat_service.py     # lógica del chatbot
```

## 5. Teoría + práctica de cada módulo

### requirements.txt

```
google-generativeai
python-dotenv
```

### .env

```
GEMINI_API_KEY=AIzaSyD************tu_clave
MODEL=gemini-1.5-flash
```

### config.py

**Teoría:** Centralizamos la configuración en una clase.

**Práctica:** Definimos Settings con dataclass → más ordenado y fácil de leer.

```python
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    api_key: str = os.getenv("GEMINI_API_KEY", "")
    model: str = os.getenv("MODEL", "")
    max_retries: int = int(os.getenv("MAX_RETRIES", "3"))  # Reintentos ante fallos
    timeout_seconds: int = int(os.getenv("TIMEOUT_SECONDS", "30"))
    max_history_messages: int = int(os.getenv("MAX_HISTORY", "12"))  # Máximo de mensajes en memoria

settings = Settings()
```

### prompts.py

```python
from typing import List, Dict

def build_system_prompt(role_instructions: str) -> str:
    base = (
        "Sos un chatbot de consola que responde en español de forma clara y útil. "
        "Si el usuario pide código, incluí explicaciones breves. "
        "Evitá información inventada y pedí aclaraciones si faltan datos.\n\n"
    )
    return base + f"Contexto de rol: {role_instructions}"

def collapse_history(history: List[Dict[str, str]]) -> List[Dict[str, str]]:
    # Mantiene formato {'role': 'user'|'model', 'content': '...'}
    # (Si quisieras sumarizar, acá podrías condensar los más viejos)
    return history
```

### memory.py

**Teoría:** La memoria se guarda en una cola circular (deque).

**Práctica:** Permitimos que el bot recuerde solo los últimos N mensajes.

```python
from collections import deque
from typing import Deque, Dict, List

class ConversationMemory:
    """
    Memoria simple en cola: guarda últimos N turnos (usuario/modelo).
    """
    def __init__(self, max_messages: int = 12):
        self._messages: Deque[Dict[str, str]] = deque(maxlen=max_messages)
    
    def add_user(self, content: str):
        self._messages.append({"role": "user", "content": content})
    
    def add_model(self, content: str):
        self._messages.append({"role": "model", "content": content})
    
    def get(self) -> List[Dict[str, str]]:
        return list(self._messages)
    
    def clear(self):
        self._messages.clear()
```

### roles.py

**Teoría:** Un rol es un conjunto de instrucciones que cambian cómo responde el bot.

**Práctica:** Ejemplo: Profesor, Traductor, Programador.

```python
from enum import Enum

class RolePreset(Enum):
    PROFESOR = "profesor"
    TRADUCTOR = "traductor"
    PROGRAMADOR = "programador"
    ASISTENTE = "asistente"

ROLE_SYSTEM_PROMPTS = {
    RolePreset.PROFESOR: (
        "Actuá como profesor paciente y claro. Explicá con ejemplos simples, "
        "resumí al final con bullets de 2-4 puntos."
    ),
    RolePreset.TRADUCTOR: (
        "Sos un traductor profesional. Mantené el significado, tono y formato. "
        "Si hay ambigüedad, ofrecé dos opciones."
    ),
    RolePreset.PROGRAMADOR: (
        "Sos un desarrollador senior. Respondé conciso, con mejores prácticas, "
        "fragmentos de código mínimos y razones de diseño."
    ),
    RolePreset.ASISTENTE: (
        "Sos un asistente general, cordial y directo. Priorizá utilidad y claridad."
    ),
}
```

### llm_client.py

**Teoría:** Es el puente con la API de Gemini.

**Práctica:** Implementamos reintentos automáticos en caso de error.

```python
import time
from typing import Dict, List, Optional
import google.generativeai as genai
from config import settings

class GeminiClient:
    def __init__(self, api_key: str, model_name: str):
        if not api_key:
            raise ValueError("GEMINI_API_KEY no está configurada.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
    
    def generate(
        self,
        system_prompt: str,
        history: List[Dict[str, str]],
        user_message: str,
        max_retries: int,
        timeout_seconds: int
    ) -> str:
        """
        Manejo de errores con reintentos y backoff exponencial simple.
        """
        attempt = 0
        last_error: Optional[Exception] = None
        
        # Preparamos el historial como una conversación del SDK
        convo = self.model.start_chat(
            history=[{"role": "user", "parts": system_prompt}] +
                    [{"role": m["role"], "parts": m["content"]} for m in history]
        )
        
        while attempt < max_retries:
            try:
                response = convo.send_message(user_message)
                text = getattr(response, "text", "")
                if not text:
                    raise RuntimeError("Respuesta vacía del modelo.")
                return text
            except Exception as e:
                last_error = e
                sleep_s = 2 ** attempt  # 1, 2, 4...
                time.sleep(sleep_s)
                attempt += 1
        
        raise RuntimeError(f"Fallo tras {max_retries} reintentos. Último error: {last_error}")
```

### chat_service.py

**Teoría:** Es el cerebro que conecta memoria + roles + cliente de Gemini.

**Práctica:** Maneja historial, agrega mensajes y devuelve la respuesta.

```python
from typing import Optional
from config import settings
from roles import RolePreset, ROLE_SYSTEM_PROMPTS
from prompts import build_system_prompt, collapse_history
from memory import ConversationMemory
from llm_client import GeminiClient

class ChatService:
    def __init__(self, role: RolePreset = RolePreset.ASISTENTE):
        self.role = role
        self.memory = ConversationMemory(max_messages=settings.max_history_messages)
        self.client = GeminiClient(api_key=settings.api_key, model_name=settings.model)
    
    def set_role(self, role: RolePreset):
        self.role = role
    
    def ask(self, prompt: str) -> str:
        # Construye contexto de sistema según rol
        system_prompt = build_system_prompt(ROLE_SYSTEM_PROMPTS[self.role])
        
        # Historial (colapsado/sumarizado si hace falta)
        history = collapse_history(self.memory.get())
        
        # Enviar
        response_text = self.client.generate(
            system_prompt=system_prompt,
            history=history,
            user_message=prompt,
            max_retries=settings.max_retries,
            timeout_seconds=settings.timeout_seconds
        )
        
        # Actualizar memoria
        self.memory.add_user(prompt)
        self.memory.add_model(response_text)
        
        return response_text
    
    def reset(self):
        self.memory.clear()
```

### main.py

**Teoría:** Creamos una interfaz de consola para interactuar con el bot.

**Práctica:** Comandos: :rol, :reset, :salir.

```python
import sys
from roles import RolePreset
from chat_service import ChatService
from config import settings

def choose_role() -> RolePreset:
    print("Elegí un rol inicial:")
    print("1) Profesor 2) Traductor 3) Programador 4) Asistente")
    sel = input("> ").strip()
    mapping = {
        "1": RolePreset.PROFESOR,
        "2": RolePreset.TRADUCTOR,
        "3": RolePreset.PROGRAMADOR,
        "4": RolePreset.ASISTENTE,
    }
    return mapping.get(sel, RolePreset.ASISTENTE)

def print_help():
    print("\nComandos:")
    print(":rol profesor|traductor|programador|asistente -> cambia el rol")
    print(":reset -> limpia la memoria")
    print(":salir -> termina\n")

def main():
    print("🤖 Chatbot con Gemini II")
    role = choose_role()
    chat = ChatService(role=role)
    print_help()
    
    while True:
        try:
            user = input("🧑 Vos: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Chau!")
            break
        
        if not user:
            continue
        
        # Comandos
        if user.lower() in (":salir", "salir", "exit", "quit"):
            print("👋 ¡Chau!")
            break
        
        if user.lower() == ":reset":
            chat.reset()
            print("🧼 Memoria borrada.")
            continue
        
        if user.lower().startswith(":rol"):
            _, *rest = user.split()
            new_role = (rest[0] if rest else "").lower()
            mapping = {
                "profesor": RolePreset.PROFESOR,
                "traductor": RolePreset.TRADUCTOR,
                "programador": RolePreset.PROGRAMADOR,
                "asistente": RolePreset.ASISTENTE,
            }
            if new_role in mapping:
                chat.set_role(mapping[new_role])
                print(f"🎭 Rol cambiado a: {new_role}")
            else:
                print("⚠️ Rol inválido. Opciones: profesor, traductor, programador, asistente.")
            continue
        
        if user.lower() == ":help":
            print_help()
            continue
        
        # Pregunta normal
        try:
            answer = chat.ask(user)
            print("🤖 Bot:", answer)
        except Exception as e:
            print("❌ Error manejado:", e)

if __name__ == "__main__":
    main()
```

## 6. Relación con lo que ya vimos en clase

- **Git y GitHub:** todo este proyecto se debe versionar y subir a GitHub.
- **Inteligencia Artificial:** este chatbot es un caso práctico de IA aplicada a asistentes.
- **APIs:** Gemini lo usamos mediante una API, un "puente" para conectar programas.

## 7. Correr el programa

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
python main.py
```
