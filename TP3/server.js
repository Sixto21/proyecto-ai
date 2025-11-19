// Servidor básico con Node.js y Express - TP3
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static('public'));

// Ruta principal
app.get('/', (req, res) => {
    res.send(`
        <html>
            <head>
                <title>Servidor Node.js - TP3</title>
                <style>
                    body { font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; background: #f0f0f0; }
                    h1 { color: #333; }
                    .card { background: white; padding: 20px; margin: 10px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
                    a { color: #007bff; text-decoration: none; }
                    a:hover { text-decoration: underline; }
                </style>
            </head>
            <body>
                <h1>🚀 Servidor Node.js - TP3</h1>
                <div class="card">
                    <h2>Bienvenido</h2>
                    <p>Este es un servidor web básico creado con Node.js y Express</p>
                </div>
                <div class="card">
                    <h3>Rutas disponibles:</h3>
                    <ul>
                        <li><a href="/api/info">/api/info</a> - Información del servidor</li>
                        <li><a href="/api/saludo/TuNombre">/api/saludo/[nombre]</a> - Saludo personalizado</li>
                        <li><a href="/api/hora">/api/hora</a> - Hora actual</li>
                        <li><a href="/api/datos">/api/datos</a> - Datos de ejemplo</li>
                    </ul>
                </div>
            </body>
        </html>
    `);
});

app.get('/api/info', (req, res) => {
    res.json({
        nombre: 'Servidor Node.js TP3',
        version: '1.0.0',
        tecnologias: ['Node.js', 'Express', 'JavaScript']
    });
});

app.get('/api/saludo/:nombre', (req, res) => {
    res.json({
        mensaje: `¡Hola ${req.params.nombre}!`,
        timestamp: new Date().toLocaleString()
    });
});

app.get('/api/hora', (req, res) => {
    res.json({
        fecha: new Date().toLocaleDateString(),
        hora: new Date().toLocaleTimeString()
    });
});

app.get('/api/datos', (req, res) => {
    res.json({
        usuarios: [
            { id: 1, nombre: 'Juan', edad: 25 },
            { id: 2, nombre: 'María', edad: 30 }
        ]
    });
});

app.listen(port, () => {
    console.log(`✅ Servidor en http://localhost:${port}`);
});
