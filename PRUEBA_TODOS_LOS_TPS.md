# Guía de Prueba - Todos los TPs

## TP1 - Fundamentos de IA y Git
**Archivos para revisar:**
- `inteligencia_artificial.md` - Abrir y leer
- `guia_gitlab.md` - Abrir y leer

✅ Solo lectura, no requiere ejecución

---

## TP2 - Chatbot con Gemini
**Para ejecutar:**
```bash
cd TP2
python main.py
```

**Requisitos:**
1. Crear archivo `.env` con tu API key de Gemini
2. Instalar dependencias: `pip install -r requirements.txt`

**Archivos:**
- `main.py` - Chatbot funcional
- `guia_chatbot_gemini.md` - Documentación

---

## TP3 - Node.js con TypeScript
**Para ejecutar:**
```bash
cd TP3
npm install
npm start
```

**Archivos:**
- `server.js` - Servidor Express
- `package.json` - Configuración
- `guia_nodejs_typescript.md` - Tutorial completo

**Prueba:** Abre http://localhost:3000

---

## TP4 - Chatbot Estructurado (Backend con TypeScript)
**Para ejecutar:**
```bash
cd TP4
# (Seguir pasos de la guía para estructura completa)
```

**Archivos:**
- `guia_chatbot_estructurado.md` - Proyecto completo con estructura modular

---

## TP5 - Chatbot Avanzado con Gemini II
**Para ejecutar:**
```bash
cd TP5
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

**Archivos:**
- `guia_chatbot_gemini_avanzado.md` - Documentación completa
- Incluye: config.py, memory.py, roles.py, etc.

---

## TP6 - Frontend Flask + Bootstrap
**Para ejecutar:**
```bash
cd TP6
pip install -r requirements.txt
python app.py
```

**Archivos:**
- `app.py` - Servidor Flask ✅ (YA FUNCIONANDO)
- `templates/index.html` - Interfaz web
- `guia_frontend_flask_bootstrap.md` - Documentación

**Prueba:** Abre http://localhost:5000 ✅

---

## Verificación Rápida de Todos los TPs

```powershell
# TP1 - Revisar documentos
cd TP1
notepad inteligencia_artificial.md

# TP2 - Chatbot Gemini (requiere API key)
cd ..\TP2
python main.py

# TP3 - Node.js (requiere npm install)
cd ..\TP3
npm start

# TP6 - Flask (el más fácil de probar)
cd ..\TP6
python app.py
```
