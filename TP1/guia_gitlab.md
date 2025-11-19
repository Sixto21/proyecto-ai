# Guía de GitLab

## ¿Qué es Git y qué es GitLab?

**Git**: Sistema de control de versiones que permite:
- Guardar versiones de código
- Volver a estados anteriores
- Trabajar en equipo sin pisarse el trabajo

**GitLab**: Plataforma basada en Git, permite alojar repositorios, colaborar en equipo, automatizar tareas, CI/CD, etc.

## Crear una cuenta en GitLab

1. Ir a https://gitlab.com
2. Registrarse con email o cuenta de GitHub/Google
3. Confirmar correo electrónico
4. Elegir nombre de usuario, Configurar perfil, etc.

## Crear un nuevo proyecto

1. Click en 'New project'
2. Elegir 'Create blank project'
3. Completar nombre del proyecto y visibilidad
4. Click en 'Create project'

## Clonar el repositorio localmente

Requiere tener Git instalado.

**Comandos:**
```bash
git clone https://gitlab.com/usuario/proyecto-clase.git
cd proyecto-clase
```

## Primer commit

```bash
echo "# Proyecto clase" > README.md
git add README.md
git commit -m "Primer commit"
git push origin main
```

## Crear una rama

```bash
git checkout -b feature/nueva-funcionalidad
# Crear nuevo archivo
echo "Proyecto clase" > archivo.txt
git add archivo.txt
git add .
git commit -m "Agregado archivo en nueva rama"
git push origin feature/nueva-funcionalidad
```

## Merge Request en GitLab

1. Ir al proyecto en GitLab
2. Verás una sugerencia para crear un MR desde la nueva rama o seleccionar 'Merge Requests' > 'New merge request'
3. Completar título y descripción
4. Crear merge request y revisar
5. Aprobar y hacer Merge

## Buenas prácticas

- Usar ramas para nuevas funcionalidades
- Hacer commits pequeños y descriptivos
- No trabajar directamente en main
- Revisar código antes de merge

---

## Actividad práctica

1. Crear repo sobre AI
2. Subir archivo lo que saben de AI
3. Crear rama feature/AI
4. Editar archivo
5. Hacer merge request
6. Crear nueva Rama machine learning
7. Crear archivo, investigar, y colocar que entienden por machine learning

---
*Prof. Vassallo Nicolás*
