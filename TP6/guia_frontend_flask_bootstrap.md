# Creación del Front-End con Flask y Bootstrap para el Chatbot con Gemini

*Prof. Nicolás Vassallo*

En este tutorial vamos a construir el front-end del proyecto de chatbot con Gemini. El back-end ya está definido en la clase anterior, pero en este documento nos concentraremos en crear una interfaz web moderna utilizando Flask y Bootstrap. El objetivo es tener una interfaz profesional, modular y lista para conectarse al back-end.

## Paso 1: Instalar dependencias

Agregamos Flask al archivo `requirements.txt`:
```
Flask>=3.0
```

Luego instalamos las dependencias:
```bash
pip install -r requirements.txt
```

## Paso 2: Estructura del Front-End

Creamos una carpeta `webapp` dentro del proyecto con la siguiente estructura:

```
chatbot-gemini/
├─ webapp/
│  ├─ __init__.py
│  ├─ routes.py
│  ├─ templates/
│  │  ├─ base.html
│  │  └─ chat.html
│  └─ static/
│     ├─ css/app.css
│     └─ js/app.js
└─ run_front.py
```

## Paso 3: Archivo run_front.py

Este archivo permite iniciar el front-end:

```python
# run_front.py
from webapp import create_app

app = create_app()

if __name__ == "__main__":
    # Debug solo para desarrollo
    app.run(host="127.0.0.1", port=5000, debug=True)
```

## Paso 4: Configuración de Flask (__init__.py)

Definimos una factory que crea la aplicación y registra las rutas:

```python
# webapp/__init__.py
from flask import Flask
from .routes import ui_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(ui_bp)
    return app
```

## Paso 5: Definición de rutas (routes.py)

Creamos un Blueprint con las rutas de la interfaz:

```python
# webapp/routes.py
from flask import Blueprint, render_template

ui_bp = Blueprint("ui", __name__, template_folder="templates", static_folder="static")

@ui_bp.get("/")
def home():
    # Página principal del chat
    return render_template("chat.html")

@ui_bp.get("/about")
def about():
    # Podés sumar una pantalla "Acerca de" si querés
    return render_template("base.html", content="Acá iría info del proyecto.")
```

## Paso 6: Template base (base.html)

Este template define la estructura principal y carga Bootstrap:

```html
<!-- webapp/templates/base.html -->
<!doctype html>
<html lang="es" data-bs-theme="light">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Chatbot con Gemini — Front</title>
    
    <!-- Bootstrap 5 (CDN) -->
    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
    
    <!-- Estilos propios -->
    <link rel="stylesheet" href="{{ url_for('ui.static', filename='css/app.css') }}">
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top shadow-sm">
        <div class="container">
            <a class="navbar-brand fw-semibold" href="/">🤖 Chatbot Gemini (Front)</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div id="nav" class="collapse navbar-collapse">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="/">Chat</a></li>
                    <li class="nav-item"><a class="nav-link" href="/about">Acerca de</a></li>
                </ul>
            </div>
        </div>
    </nav>
    
    <!-- Contenido -->
    <main class="py-4">
        <div class="container">
            {% block content %}{% endblock %}
        </div>
    </main>
    
    <!-- Toasts -->
    <div class="position-fixed bottom-0 end-0 p-3" style="z-index: 1080">
        <div id="app-toast" class="toast align-items-center border-0" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div id="app-toast-body" class="toast-body"></div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        </div>
    </div>
    
    <!-- Bootstrap JS + Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- JS propio -->
    <script src="{{ url_for('ui.static', filename='js/app.js') }}"></script>
</body>
</html>
```

## Paso 7: Pantalla de chat (chat.html)

Extiende de base.html y muestra la interfaz de chat:

```html
<!-- webapp/templates/chat.html -->
{% extends "base.html" %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-12 col-lg-8">
        <div class="card shadow-lg border-0">
            <div class="card-header d-flex flex-wrap gap-2 align-items-center">
                <span class="fw-semibold me-auto">Chat</span>
                
                <!-- Selector de Rol (solo UI por ahora) -->
                <div class="d-flex align-items-center gap-2">
                    <label for="roleSelect" class="form-label m-0 small text-muted">Rol</label>
                    <select id="roleSelect" class="form-select form-select-sm">
                        <option value="asistente" selected>Asistente</option>
                        <option value="profesor">Profesor</option>
                        <option value="traductor">Traductor</option>
                        <option value="programador">Programador</option>
                    </select>
                </div>
                
                <button id="btnClear" class="btn btn-outline-secondary btn-sm">
                    Limpiar
                </button>
            </div>
            
            <div id="chatBody" class="card-body chat-body">
                <!-- Mensajes renderizados por JS -->
            </div>
            
            <div class="card-footer">
                <form id="chatForm" class="d-flex gap-2">
                    <input
                        id="chatInput"
                        class="form-control"
                        type="text"
                        placeholder="Escribí tu mensaje..."
                        autocomplete="off"
                    />
                    <button id="btnSend" class="btn btn-primary" type="submit">
                        Enviar
                    </button>
                </form>
                <small class="text-muted">
                    * Esta versión usa <strong>mock del lado del cliente</strong>. No hay conexión con el backend aún.
                </small>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## Paso 8: Estilos (app.css)

Definimos burbujas para usuario y bot:

```css
/* webapp/static/css/app.css */

/* Altura cómoda y scroll interno */
.chat-body {
    height: 60vh;
    overflow-y: auto;
    background: #f8f9fa;
}

/* Mensajes */
.message {
    max-width: 85%;
    padding: .6rem .8rem;
    border-radius: 1rem;
    margin-bottom: .5rem;
    white-space: pre-wrap;
    word-wrap: break-word;
}

.message.user {
    margin-left: auto;
    background: #0d6efd;
    color: #fff;
    border-bottom-right-radius: .25rem;
}

.message.bot {
    margin-right: auto;
    background: #ffffff;
    color: #212529;
    border: 1px solid #e9ecef;
    border-bottom-left-radius: .25rem;
}

/* Meta (hora, rol) */
.message small {
    display: block;
    opacity: .7;
    margin-top: .2rem;
    font-size: .75rem;
}

/* "Escribiendo..." */
.typing {
    display: inline-block;
    width: .6rem;
    height: .6rem;
    border-radius: 50%;
    background: #adb5bd;
    margin: 0 .15rem;
    animation: blink 1.2s infinite ease-in-out;
}

.typing:nth-child(2) { animation-delay: .2s; }
.typing:nth-child(3) { animation-delay: .4s; }

@keyframes blink {
    0%, 80%, 100% { opacity: .2; }
    40% { opacity: 1; }
}
```

## Paso 9: Lógica de chat en JS (app.js)

El JavaScript maneja el envío del formulario y agrega mensajes al chat. Por ahora usa un mock de respuesta en el navegador:

```javascript
// webapp/static/js/app.js
(function () {
    // --------------------------
    // Utilidades
    // --------------------------
    const $ = (sel) => document.querySelector(sel);
    const formatTime = (d = new Date()) =>
        d.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

    // --------------------------
    // Store (LocalStorage)
    // --------------------------
    const Store = {
        KEY_MESSAGES: "cg_chat_messages",
        KEY_ROLE: "cg_chat_role",
        
        getMessages() {
            try {
                return JSON.parse(localStorage.getItem(this.KEY_MESSAGES) || "[]");
            } catch {
                return [];
            }
        },
        setMessages(list) {
            localStorage.setItem(this.KEY_MESSAGES, JSON.stringify(list));
        },
        addMessage(msg) {
            const list = this.getMessages();
            list.push(msg);
            this.setMessages(list);
        },
        clear() {
            localStorage.removeItem(this.KEY_MESSAGES);
        },
        getRole() {
            return localStorage.getItem(this.KEY_ROLE) || "asistente";
        },
        setRole(role) {
            localStorage.setItem(this.KEY_ROLE, role);
        },
    };

    // --------------------------
    // Mock del "modelo"
    // --------------------------
    const MockLLM = {
        async reply(userText, role) {
            // Simula latencia
            await new Promise((r) => setTimeout(r, 600));
            
            // Respuesta sencilla según "rol" (solo para UI)
            const roleHint = {
                profesor:
                    "Explicación breve: dividí el problema en partes simples y recordá ejemplos.",
                traductor:
                    "Traducción: (esto es un ejemplo) → "Hello! This is a mock translation."",
                programador:
                    "Sugerencia técnica: preferí funciones puras y manejo de errores claro.",
                asistente:
                    "Tip: si necesitás más contexto, podés ampliar tu pregunta.",
            }[role] || "";
            
            const echo = userText.trim().length
                ? `Entendí: "${userText.trim()}"`
                : "Recibí tu mensaje, ¿podés contármelo con más detalle?";
            
            return `${echo}\n${roleHint}`;
        },
    };

    // --------------------------
    // Toast helper (Bootstrap)
    // --------------------------
    function showToast(msg) {
        const toastEl = $("#app-toast");
        const bodyEl = $("#app-toast-body");
        if (!toastEl || !bodyEl) return;
        
        bodyEl.textContent = msg;
        const t = new bootstrap.Toast(toastEl, { delay: 2200 });
        t.show();
    }

    // --------------------------
    // ChatUI
    // --------------------------
    const ChatUI = {
        els: {
            body: $("#chatBody"),
            form: $("#chatForm"),
            input: $("#chatInput"),
            btnSend: $("#btnSend"),
            btnClear: $("#btnClear"),
            role: $("#roleSelect"),
        },

        init() {
            // Rol guardado
            this.els.role.value = Store.getRole();
            this.bindEvents();
            this.renderAll(Store.getMessages());
            this.scrollToEnd();
            
            if (Store.getMessages().length === 0) {
                this.pushBot("¡Hola! Esta es la interfaz del chatbot.\nPor ahora es un mock visual, sin backend.");
            }
        },

        bindEvents() {
            this.els.form.addEventListener("submit", (e) => {
                e.preventDefault();
                this.handleSend();
            });
            
            this.els.btnClear.addEventListener("click", () => {
                Store.clear();
                this.els.body.innerHTML = "";
                this.pushBot("Memoria local borrada. Empecemos de nuevo. 🙂");
            });
            
            this.els.role.addEventListener("change", (e) => {
                Store.setRole(e.target.value);
                showToast(`Rol cambiado a: ${e.target.value}`);
            });
        },

        async handleSend() {
            const text = (this.els.input.value || "").trim();
            if (!text) return;
            
            // Pintar mensaje del usuario
            this.pushUser(text);
            this.els.input.value = "";
            this.scrollToEnd();
            
            // "Escribiendo…"
            const typingId = this.pushTyping();
            
            // Mock de respuesta
            const role = Store.getRole();
            const reply = await MockLLM.reply(text, role);
            
            // Remplazar "typing…" y pintar respuesta
            this.removeTyping(typingId);
            this.pushBot(reply);
            this.scrollToEnd();
        },

        pushUser(text) {
            const msg = { role: "user", text, time: formatTime() };
            Store.addMessage(msg);
            this.renderMessage(msg);
        },

        pushBot(text) {
            const msg = { role: "bot", text, time: formatTime() };
            Store.addMessage(msg);
            this.renderMessage(msg);
        },

        pushTyping() {
            const id = `typing-${Date.now()}`;
            const wrap = document.createElement("div");
            wrap.className = "message bot";
            wrap.id = id;
            wrap.innerHTML = `
                <div>
                    <span class="typing"></span>
                    <span class="typing"></span>
                    <span class="typing"></span>
                </div>
                <small>${formatTime()}</small>
            `;
            this.els.body.appendChild(wrap);
            return id;
        },

        removeTyping(id) {
            const el = document.getElementById(id);
            if (el) el.remove();
        },

        renderAll(list) {
            this.els.body.innerHTML = "";
            list.forEach((m) => this.renderMessage(m));
        },

        renderMessage({ role, text, time }) {
            const div = document.createElement("div");
            div.className = `message ${role}`;
            div.innerHTML = `
                <div>${escapeHtml(text)}</div>
                <small>${role === "user" ? "Vos" : "Bot"} • ${time}</small>
            `;
            this.els.body.appendChild(div);
        },

        scrollToEnd() {
            this.els.body.scrollTop = this.els.body.scrollHeight;
        },
    };

    // Seguridad básica para inyectar texto
    function escapeHtml(str) {
        return str
            .replaceAll("&", "&amp;")
            .replaceAll("<", "&lt;")
            .replaceAll(">", "&gt;");
    }

    // Init
    document.addEventListener("DOMContentLoaded", () => ChatUI.init());
})();
```

## Paso 10: Probar el proyecto

Ejecutar:
```bash
python run_front.py
```

Abrir http://127.0.0.1:5000 en el navegador. Deberías ver la interfaz de chat con Bootstrap y respuestas simuladas.
