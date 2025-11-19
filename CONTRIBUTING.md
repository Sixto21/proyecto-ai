# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto! Aquí te explico cómo hacerlo.

## 📋 Código de Conducta

Este proyecto se adhiere a un código de conducta profesional. Al participar, se espera que mantengas un ambiente respetuoso y colaborativo.

## 🔧 Proceso de Contribución

### 1. Fork del Proyecto
```bash
# Haz un fork desde GitLab y luego clona tu fork
git clone https://gitlab.com/TU_USUARIO/proyecto-ai.git
cd proyecto-ai
```

### 2. Crea una Rama
```bash
# Crea una rama descriptiva para tu cambio
git checkout -b feature/nombre-descriptivo
```

### 3. Realiza tus Cambios
- Escribe código limpio y comentado
- Sigue las convenciones del proyecto
- Prueba tus cambios localmente

### 4. Commit de tus Cambios
```bash
git add .
git commit -m "feat: descripción clara del cambio"
```

**Formato de mensajes de commit:**
- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de bugs
- `docs:` - Cambios en documentación
- `style:` - Formato, punto y coma, etc.
- `refactor:` - Refactorización de código
- `test:` - Agregar tests
- `chore:` - Tareas de mantenimiento

### 5. Push y Merge Request
```bash
git push origin feature/nombre-descriptivo
```

Luego crea un **Merge Request** en GitLab con:
- Título descriptivo
- Descripción detallada de los cambios
- Referencias a issues relacionados (si aplica)

## 🧪 Testing

Antes de hacer un MR, asegúrate de:
- [ ] El código funciona correctamente
- [ ] No hay errores de sintaxis
- [ ] Las dependencias están actualizadas en `requirements.txt` o `package.json`
- [ ] La documentación está actualizada

## 📝 Estándares de Código

### Python
- Sigue [PEP 8](https://pep8.org/)
- Usa nombres descriptivos para variables y funciones
- Documenta funciones complejas con docstrings

### JavaScript/TypeScript
- Usa `const` y `let`, evita `var`
- Nombres en camelCase para variables
- Comentarios claros y concisos

### Markdown
- Usa títulos jerárquicos (H1, H2, H3)
- Incluye bloques de código con sintaxis resaltada
- Enlaces funcionales y actualizados

## 🐛 Reportar Bugs

Si encuentras un bug, abre un **Issue** con:
1. **Título claro** del problema
2. **Pasos para reproducir** el error
3. **Comportamiento esperado** vs **comportamiento actual**
4. **Capturas de pantalla** (si aplica)
5. **Entorno** (OS, versión de Python/Node, etc.)

## 💡 Sugerencias de Mejoras

Para proponer nuevas funcionalidades:
1. Abre un **Issue** con etiqueta `enhancement`
2. Describe el problema que resuelve
3. Propón una solución técnica
4. Espera feedback antes de implementar

## 📧 Contacto

Si tienes dudas, puedes:
- Abrir un Issue en GitLab
- Contactar al autor: [elmercado09-group](https://gitlab.com/elmercado09-group)

---

¡Gracias por contribuir! 🎉
