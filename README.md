# Validador de CURP - Máquina de Turing

## 🎯 Descripción
Un simulador visual de una Máquina de Turing implementado en Python que valida la estructura de la Clave Única de Registro de Población (CURP) mexicana. El proyecto demuestra la aplicación práctica de los conceptos de teoría de la computación y autómatas.

## ✨ Características
- Interfaz gráfica moderna e intuitiva
- Visualización paso a paso del proceso de validación
- Representación visual de la cinta de la Máquina de Turing
- Feedback visual del estado de validación
- Manejo de errores robusto

## 🔧 Requisitos
- Python 3.x
- Tkinter (GUI)

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/betooxx-dev/lya-curp.git
```

2. Instala las dependencias necesarias:
```bash
sudo apt install python3-tk
```

3. Ejecuta el programa:
```bash
python3 main.py
```

## 🚀 Uso
1. Inicia la aplicación
2. Ingresa una CURP en el campo de texto
3. Presiona el botón "Validar"
4. Observa el proceso de validación en la visualización de la cinta
5. Recibe el resultado de la validación

## 🤖 Cómo Funciona
La máquina de Turing implementada sigue las reglas oficiales de formación de la CURP:
- Primer letra y vocal del primer apellido
- Primera letra del segundo apellido
- Primera letra del nombre
- Fecha de nacimiento (AAMMDD)
- Sexo (H/M)
- Estado de nacimiento (2 letras)
- Primera consonante interna del primer apellido
- Primera consonante interna del segundo apellido
- Primera consonante interna del nombre
- Caracteres de homoclave

## 📝 Estructura del Proyecto
```
validador-curp-turing/
├── main.py              # Punto de entrada y GUI
├── README.md           # Documentación
```