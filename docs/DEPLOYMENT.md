# 🚀 Guía de Deployment

Esta guía explica cómo desplegar cada TP en diferentes plataformas.

## 📋 Tabla de Contenidos
1. [TP2 - Chatbot Gemini en Railway](#tp2---railway)
2. [TP3 - API Node.js en Render](#tp3---render)
3. [TP6 - Flask App en Heroku](#tp6---heroku)
4. [Docker Deployment](#docker-deployment)

---

## TP2 - Chatbot Gemini en Railway

### 1. Preparación
```bash
cd TP2
# Asegúrate de tener requirements.txt
pip freeze > requirements.txt
```

### 2. Crear `Procfile`
```
worker: python main.py
```

### 3. Deploy en Railway
1. Ve a [railway.app](https://railway.app/)
2. Conecta tu repo de GitLab
3. Selecciona carpeta `TP2`
4. Agrega variable de entorno: `GEMINI_API_KEY`
5. Deploy automático ✅

---

## TP3 - API Node.js en Render

### 1. Preparación
```bash
cd TP3
# Asegúrate de tener start script en package.json
```

### 2. Actualizar `package.json`
```json
{
  "scripts": {
    "start": "node server.js"
  }
}
```

### 3. Deploy en Render
1. Ve a [render.com](https://render.com/)
2. New → Web Service
3. Conecta GitLab repo
4. Root directory: `TP3`
5. Build command: `npm install`
6. Start command: `npm start`
7. Deploy ✅

---

## TP6 - Flask App en Heroku

### 1. Preparación
```bash
cd TP6

# Crear Procfile
echo "web: python app.py" > Procfile

# Asegurarse que app.py use puerto de Heroku
# Cambiar: app.run(port=5000)
# Por: app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

### 2. Deploy en Heroku
```bash
# Instalar Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Crear app
heroku create mi-chatbot-ia

# Deploy
git subtree push --prefix TP6 heroku main

# Ver logs
heroku logs --tail
```

### 3. Configurar variables de entorno
```bash
heroku config:set GEMINI_API_KEY=tu_clave_aqui
```

---

## Docker Deployment

### TP6 - Dockerfile
```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Construir y correr
```bash
cd TP6

# Construir imagen
docker build -t chatbot-ia .

# Correr contenedor
docker run -p 5000:5000 -e GEMINI_API_KEY=tu_clave chatbot-ia
```

### Docker Compose (múltiples TPs)
```yaml
version: '3.8'

services:
  tp2-chatbot:
    build: ./TP2
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    restart: unless-stopped

  tp3-api:
    build: ./TP3
    ports:
      - "3000:3000"
    restart: unless-stopped

  tp6-web:
    build: ./TP6
    ports:
      - "5000:5000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    restart: unless-stopped
```

---

## Vercel (Frontend estático)

Si quieres desplegar solo el frontend de TP6:

### 1. Extraer archivos estáticos
```bash
cd TP6
mkdir static-site
cp templates/index.html static-site/
# Modificar para no usar Flask, usar API mock
```

### 2. Deploy
```bash
# Instalar Vercel CLI
npm i -g vercel

# Deploy
vercel
```

---

## Variables de Entorno

### Archivo `.env.production`
```bash
GEMINI_API_KEY=AIzaSy...
FLASK_ENV=production
SECRET_KEY=clave_secreta_aleatoria
DEBUG=False
```

### GitLab CI/CD Variables
1. Ve a Settings → CI/CD → Variables
2. Agrega:
   - `GEMINI_API_KEY` (protected, masked)
   - `HEROKU_API_KEY` (para deploy automático)

---

## SSL/HTTPS

### Usar Cloudflare (gratis)
1. Registra tu dominio en Cloudflare
2. Configura DNS apuntando a Heroku/Railway
3. SSL automático ✅

### Let's Encrypt (self-hosted)
```bash
# Si usas servidor propio
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d tudominio.com
```

---

## Monitoreo

### Heroku Logs
```bash
heroku logs --tail --app mi-chatbot-ia
```

### Railway Logs
- Dashboard → Project → Deployments → View Logs

### Render Logs
- Dashboard → Service → Logs (live stream)

---

## Troubleshooting

### Error: "Application Error"
- Verificar Procfile
- Revisar logs: `heroku logs --tail`
- Verificar variables de entorno

### Error: "Port already in use"
```python
# Usar puerto dinámico
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

### Error: "Module not found"
```bash
# Regenerar requirements.txt
pip freeze > requirements.txt
git add requirements.txt
git commit -m "fix: actualizar dependencias"
git push
```

---

## Checklist Pre-Deploy ✅

- [ ] Variables de entorno configuradas
- [ ] Dependencias actualizadas (requirements.txt / package.json)
- [ ] Puerto dinámico configurado
- [ ] .gitignore configurado (no subir .env)
- [ ] README con instrucciones
- [ ] Logs funcionando
- [ ] Prueba local con `heroku local` o `docker run`

---

**¡Listo para producción!** 🚀
