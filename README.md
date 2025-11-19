# 🤖 Proyecto IA - Desarrollo de Chatbots con IA

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-green?logo=flask&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-TypeScript-yellow?logo=node.js&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google-Gemini%20AI-orange?logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-red)

> **Portfolio de Trabajos Prácticos** - Carrera de Programación  
> Desarrollo de aplicaciones de Inteligencia Artificial con Python, Node.js y frameworks modernos

---

## 📋 Descripción

Este repositorio contiene **6 Trabajos Prácticos completos** desarrollados durante el curso de Inteligencia Artificial y Desarrollo Web. Cada TP demuestra competencias específicas en:

- ✅ Fundamentos de IA y control de versiones con Git/GitLab
- ✅ Integración de APIs de Inteligencia Artificial (Google Gemini)
- ✅ Desarrollo backend con Python y Node.js/TypeScript
- ✅ Arquitecturas modulares y escalables
- ✅ Desarrollo frontend con Flask y Bootstrap 5
- ✅ Gestión de estado, memoria y roles en chatbots

---

## 🗂️ Estructura del Proyecto

```
proyecto-ai/
│
├── TP1/                          # Fundamentos de IA y Git
│   ├── inteligencia_artificial.md
│   ├── guia_gitlab.md
│   └── machine_learning.md
│
├── TP2/                          # Chatbot con Google Gemini
│   ├── main.py                   # Chatbot funcional con API
│   ├── guia_chatbot_gemini.md
│   ├── requirements.txt
│   └── .env.example
│
├── TP3/                          # Backend con Node.js/TypeScript
│   ├── server.js                 # Servidor Express
│   ├── guia_nodejs_typescript.md
│   └── package.json
│
├── TP4/                          # Chatbot Backend Estructurado
│   ├── chatbot_estructurado.py
│   └── guia_chatbot_estructurado.md
│
├── TP5/                          # Chatbot Avanzado con Memoria
│   ├── chatbot_mejorado.py       # Sistema modular con roles
│   └── guia_chatbot_gemini_avanzado.md
│
└── TP6/                          # Frontend Web con Flask
    ├── app.py                    # Servidor Flask
    ├── templates/index.html      # Interfaz Bootstrap 5
    ├── guia_frontend_flask_bootstrap.md
    └── requirements.txt
```

---

## 🚀 Tecnologías Utilizadas

### Backend
- **Python 3.13** - Lenguaje principal para chatbots
- **Flask 3.0+** - Framework web para frontend
- **Google Gemini AI** - Modelo de lenguaje (LLM)
- **python-dotenv** - Gestión de variables de entorno

### Frontend
- **Bootstrap 5.3.3** - Framework CSS responsive
- **JavaScript ES6+** - Lógica del cliente
- **LocalStorage API** - Persistencia de datos

### Backend Alternativo
- **Node.js** - Entorno de ejecución JavaScript
- **TypeScript** - Tipado estático para JavaScript
- **Express.js** - Framework para APIs REST

### Control de Versiones
- **Git** - Sistema de control de versiones
- **GitLab** - Plataforma de repositorios remotos

---

## 📦 Instalación y Uso

### Requisitos Previos
```bash
# Python 3.13 o superior
python --version

# Node.js 16+ (para TP3)
node --version

# Git
git --version
```

### Clonar el Repositorio
```bash
git clone https://gitlab.com/elmercado09-group/proyecto-ai.git
cd proyecto-ai
```

### TP2 - Chatbot con Gemini (Python)
```bash
cd TP2
pip install -r requirements.txt

# Crear archivo .env con tu API key
echo GEMINI_API_KEY=tu_clave_aqui > .env

python main.py
```

### TP3 - Servidor Node.js
```bash
cd TP3
npm install
node server.js
# Abre http://localhost:3000
```

### TP6 - Interfaz Web Flask
```bash
cd TP6
pip install -r requirements.txt
python app.py
# Abre http://localhost:5000
```

---

## 🎯 Funcionalidades Destacadas

### TP2 - Integración con IA
- ✅ Conexión real con Google Gemini API
- ✅ Gestión segura de API keys con `.env`
- ✅ Manejo de errores y reintentos

### TP5 - Chatbot Avanzado
- ✅ **Memoria de conversación** (historial persistente)
- ✅ **Sistema de roles** (profesor, traductor, programador)
- ✅ **Arquitectura modular** (config, memory, roles, prompts)
- ✅ **Comandos especiales** (/ayuda, /limpiar, /rol)

### TP6 - Frontend Interactivo
- ✅ **Interfaz moderna** con Bootstrap 5
- ✅ **Selector de roles** en tiempo real
- ✅ **Indicador de escritura** animado
- ✅ **Persistencia en navegador** (LocalStorage)
- ✅ **Diseño responsive** (móvil y desktop)

---

## 📸 Capturas de Pantalla

### TP6 - Interfaz del Chatbot
![Interfaz del chatbot con Bootstrap 5](docs/screenshot-tp6.png)
*Interfaz web responsive con selector de roles y burbujas de chat*

---

## 🧪 Testing

Cada TP incluye su propia guía de pruebas. Para un test rápido de todos:

```bash
# Ver guía completa de pruebas
cat PRUEBA_TODOS_LOS_TPS.md
```

---

## 📚 Documentación

Cada carpeta TP contiene:
- **Guía completa** en Markdown con explicaciones teóricas
- **Código fuente** comentado y documentado
- **README.md** con instrucciones específicas
- **Ejemplos de uso** y capturas

---

## 🤝 Contribuciones

Este proyecto es parte de mi portfolio académico. Si tienes sugerencias:

1. Abre un **Issue** describiendo tu idea
2. Haz un **Fork** del proyecto
3. Crea una **rama** para tu feature (`git checkout -b feature/mejora`)
4. **Commit** tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
5. **Push** a la rama (`git push origin feature/mejora`)
6. Abre un **Merge Request**

---

## 👨‍💻 Autor

**Elias Mercado**  
📧 Contacto: [elmercado09-group](https://gitlab.com/elmercado09-group)  
🎓 Carrera de Programación  
📅 Curso: 2025

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

- **Prof. Nicolás Vassallo** - Autor de las guías y materiales del curso
- **Google AI** - Por proporcionar acceso a Gemini API
- **Comunidad de GitLab** - Por las herramientas de colaboración

---

## 🔗 Enlaces Útiles

- [Documentación de Google Gemini](https://ai.google.dev/)
- [Guía de Flask](https://flask.palletsprojects.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)

---

**⭐ Si este proyecto te resulta útil, dale una estrella al repositorio!**
