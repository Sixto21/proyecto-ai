# Curso Fundamentos de Node.js con TypeScript

*Prof. Nicolás Vassallo*

## 1: Introducción a Node.js

Node.js es un entorno de ejecución para JavaScript fuera del navegador. Utiliza el motor V8 de Chrome para ejecutar el código en el servidor, lo cual permite construir aplicaciones del lado backend usando JavaScript.

En este curso trabajaremos con **TypeScript (TS)**, que es un superset de JavaScript con tipado estático. Nos ayuda a evitar errores y a escribir código más mantenible.

**Verificá que Node.js y npm estén instalados:**
```bash
node -v
npm -v
```

**Creá un archivo `hola.ts` y escribí lo siguiente:**
```typescript
// hola.ts
console.log("¡Hola mundo desde Node.js con TypeScript!");
```

**Para compilar y ejecutar el archivo:**
```bash
tsc hola.ts
node hola.js
```

---

## 2: Variables y Tipos de Datos

```typescript
// variables.ts
let nombre: string = "Nicolás";        // Cadena de texto
const edad: number = 35;                // Número
let esProgramador: boolean = true;      // Booleano
let nada: null = null;                  // Nulo
let sinValor: undefined = undefined;    // No definido

console.log(nombre, edad, esProgramador, nada, sinValor);
```

**Actividad:** Crear un archivo `datos.ts` que muestre tus datos personales.

---

## 3: Operadores y Condicionales

```typescript
// operadores.ts
let edad: number = 18;

if (edad >= 18) {
    console.log("Es mayor de edad");
} else {
    console.log("Es menor de edad");
}
```

**Actividad:** Crear un archivo `verificarEdad.ts` que imprima si puede votar.

---

## 4: Bucles

```typescript
// bucles.ts
for (let i = 1; i <= 5; i++) {
    console.log("Número:", i);  // Imprime del 1 al 5
}
```

**Actividad:** Mostrar los números pares del 0 al 20.

---

## 5: Funciones

```typescript
// funciones.ts
function saludar(nombre: string): string {
    return `Hola, ${nombre}`;
}

const sumar = (a: number, b: number): number => a + b;

console.log(saludar("Malena"));    // Saludo personalizado
console.log("Suma:", sumar(5, 3)); // Muestra el resultado de la suma
```

**Actividad:** Crear una función que diga si un número es par o impar.

---

## 6: Estructuras de Datos

```typescript
// estructuras.ts

// Arreglo (Array) de strings
let frutas: string[] = ["manzana", "banana", "pera"];
frutas.forEach(f => console.log(f)); // Recorre y muestra cada fruta

// Objeto literal (estructura tipo JSON)
let persona = {
    nombre: "Mario",
    edad: 40,
    trabaja: true
};
console.log(persona.nombre); // Muestra el nombre
```

**Actividad:** Crear un array con tus 5 videojuegos favoritos y mostrarlos. Y un json con datos de tu videojuego favorito.

---

## 7: Crear una API REST simple con Node.js + TypeScript (sin base de datos)

En este módulo aprenderás a construir una API REST básica usando Node.js con TypeScript, sin conectarse a una base de datos. La API permitirá obtener, agregar y eliminar elementos almacenados en memoria (en un array). Usaremos la biblioteca 'express'.

### Paso 1: Inicializar el proyecto

Desde la terminal, ejecuta lo siguiente:
```bash
mkdir mi-api
cd mi-api
npm init -y
npm install express
npm install --save-dev typescript ts-node @types/node @types/express
```

**Creá el archivo `tsconfig.json` con la configuración mínima:**

```json
{
    "compilerOptions": {
        "target": "ES6",
        "module": "commonjs",
        "rootDir": "./src",
        "outDir": "./dist",
        "strict": true,
        "esModuleInterop": true
    }
}
```

**Estructura del proyecto:**
```
mi-api/
├── src/
│   └── index.ts
├── package.json
└── tsconfig.json
```

### Paso 2: Crear el servidor básico

**Archivo: `src/index.ts`**

```typescript
import express, { Request, Response } from 'express';

const app = express();
const port = 3000;

// Middleware para parsear JSON
app.use(express.json());

// Datos en memoria
let tareas: string[] = [];

// Obtener todas las tareas
app.get('/tareas', (req: Request, res: Response) => {
    res.json(tareas);
});

// Agregar una nueva tarea
app.post('/tareas', (req: Request, res: Response) => {
    const { tarea } = req.body;
    tareas.push(tarea);
    res.status(201).json({ mensaje: 'Tarea agregada' });
});

// Eliminar una tarea por índice
app.delete('/tareas/:id', (req: Request, res: Response) => {
    const id = parseInt(req.params.id);
    if (id >= 0 && id < tareas.length) {
        tareas.splice(id, 1);
        res.json({ mensaje: 'Tarea eliminada' });
    } else {
        res.status(404).json({ mensaje: 'Índice inválido' });
    }
});

// Iniciar servidor
app.listen(port, () => {
    console.log(`Servidor corriendo en http://localhost:${port}`);
});
```

### Paso 3: Ejecutar la API

Desde la terminal:
```bash
npx ts-node src/index.ts
```
