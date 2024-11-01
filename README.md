# Validador y Generador de CURP - Máquina de Turing

## 🎯 Descripción
Un conjunto de herramientas basadas en Máquinas de Turing implementadas en Python para validar y generar la Clave Única de Registro de Población (CURP) mexicana. El proyecto demuestra la aplicación práctica de los conceptos de teoría de la computación y autómatas.

## ✨ Características
- Validador de CURP con interfaz gráfica moderna
- Generador de CURP automático
- Visualización paso a paso del proceso de validación
- Representación visual de la cinta de la Máquina de Turing
- Feedback visual del estado de validación
- Validación robusta de fechas y datos
- Manejo de errores detallado

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

## 🚀 Uso
### Validador de CURP - validator.py
```bash
python3 validator.py
```
1. Ingresa una CURP en el campo de texto
2. Presiona "Validar"
3. Observa el proceso de validación en la cinta
4. Recibe el resultado

### Generador de CURP - generator.py
```bash
python3 generator.py
```
1. Ingresa los datos personales requeridos:
   - Nombres y apellidos
   - Fecha de nacimiento
   - Sexo
   - Estado de nacimiento
2. Presiona "Generar CURP"
3. Recibe la CURP generada

## 🤖 Cómo Funciona
### Validador (validator.py)
Implementa una máquina de Turing que verifica la estructura correcta de una CURP existente:
- Validación de formato
- Verificación de caracteres permitidos
- Comprobación de estructura

### Generador (generator.py)
Crea una nueva CURP siguiendo las reglas oficiales:
- Primer letra y vocal del primer apellido
- Primera letra del segundo apellido
- Primera letra del nombre
- Fecha de nacimiento (AAMMDD)
- Validación de años bisiestos
- Sexo (H/M)
- Estado de nacimiento (2 letras)
- Consonantes internas
- Homoclave aleatoria válida

## 📝 Estructura del Proyecto
```
validador-curp-turing/
├── validator.py    # Validador de CURP con GUI
├── generator.py    # Generador de CURP con GUI
└── README.md      # Documentación
```