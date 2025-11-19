# Tutorial del Proyecto: mi-chatbot

*Prof. Nicolás Vassallo*

## Estructura de archivos

```
mi-chatbot/
│
├── .env                      # Variables de entorno (API KEY de Gemini)
└── src/
    ├── app.ts               # Configura Express y las rutas
    ├── routes/
    │   └── chat.routes.ts   # Define las rutas del chatbot
    └── services/
        └── gemini.service.ts # Lógica de conexión con la API de Gemini
```

## Paso 1: Instalación

```bash
npx tsc --init
```

**tsconfig.json:**
```json
{
    "compilerOptions": {
        "target": "ES2020",
        "module": "commonjs",
        "moduleResolution": "node",
        "outDir": "dist",
        "rootDir": "src",
        "strict": true,
        "esModuleInterop": true
    }
}
```

```bash
npm init -y
```

**Agregar en package.json:**
```json
"scripts": {
    "dev": "ts-node src/app.ts"
}
```

**Instalar dependencias:**
```bash
npm install express dotenv
npm install @google/generative-ai
npm install --save-dev ts-node typescript @types/express @types/node
```

## Paso 2: Configuración

En el archivo `.env`, definís tu clave de API:
```
GEMINI_API_KEY=tu_clave_secreta_de_google
```

## Paso 3: Ejecutar el proyecto

Para ejecutarlo en modo desarrollo:
```bash
npx ts-node src/app.ts
```
o
```bash
npm run dev
```

## Paso 4: Código

### 1. app.ts

Este archivo configura el servidor:

```typescript
import express from 'express';
import dotenv from 'dotenv';
import chatRoutes from './routes/chat.routes';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use('/api', chatRoutes);

app.listen(PORT, () => {
    console.log(`✅ Servidor escuchando en http://localhost:${PORT}`);
});
```

### 2. gemini.service.ts

Lógica que se conecta con Gemini:

```typescript
import * as genAI from '@google/generative-ai';
import dotenv from 'dotenv';

dotenv.config();

const API_KEY = process.env.GEMINI_API_KEY || '';
const genAIInstance = new genAI.GoogleGenerativeAI(API_KEY);
const model = genAIInstance.getGenerativeModel({ model: 'gemini-1.5-flash' });

export async function obtenerRespuesta(prompt: string): Promise<string> {
    try {
        const chat = await model.startChat();
        const result = await chat.sendMessage(prompt);
        return result.response.text();
    } catch (err) {
        console.error('Error al consultar Gemini:', err);
        return '❌ Hubo un error al obtener la respuesta.';
    }
}
```

### 3. chat.routes.ts

Define la ruta `/chat` y maneja las peticiones POST:

```typescript
import { Router, Request, Response } from 'express';
import { obtenerRespuesta } from '../services/gemini.service';

const router = Router();

router.post('/chat', async (req: Request, res: Response) => {
    const { mensaje } = req.body;
    
    if (!mensaje) {
        return res.status(400).json({ error: 'Mensaje requerido' });
    }
    
    const respuesta = await obtenerRespuesta(mensaje);
    res.json({ respuesta });
});

export default router;
```

## Ejemplo de uso (con curl)

```bash
curl -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"mensaje": "Hola, ¿quién sos?"}'
```
