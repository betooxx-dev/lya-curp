import tkinter as tk
from tkinter import ttk, messagebox, font
from ttkthemes import ThemedTk

class TuringMachine:
    def __init__(self):
        self.tape = []
        self.head_position = 0
        self.current_state = 'q0'
        self.transitions = self.initialize_transitions()
        
    def initialize_transitions(self):
        # Diccionario de transiciones: (estado_actual, símbolo_leído): (nuevo_estado, símbolo_escribir, movimiento)
        transitions = {}

        # Primeras letras de la CURP
        for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            transitions[('q0', letra)] = ('q1', letra, 'R')
        
        # Primera vocal del apellido
        transitions[('q1', 'A')] = ('q2', 'A', 'R')
        transitions[('q1', 'E')] = ('q2', 'E', 'R')
        transitions[('q1', 'I')] = ('q2', 'I', 'R')
        transitions[('q1', 'O')] = ('q2', 'O', 'R')
        transitions[('q1', 'U')] = ('q2', 'U', 'R')

        # Letras restantes del apellido
        for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            transitions[('q2', letra)] = ('q3', letra, 'R')

        # Primer letra del nombre
        for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            transitions[('q3', letra)] = ('q4', letra, 'R')

        # Primer dígito del año
        for digit in '0123456789':
            transitions[('q4', digit)] = ('q5', digit, 'R')

        # Segundo dígito del año y detección de año bisiesto
        for i in range(10):
            if i % 4 == 0:  # Años potencialmente bisiestos (00,04,08,12,16,20...)
                transitions[('q5', str(i))] = ('q6_bisiesto', str(i), 'R')
            else:
                transitions[('q5', str(i))] = ('q6_normal', str(i), 'R')

        # Mes - primer dígito
        transitions[('q6_bisiesto', '0')] = ('q7', '0', 'R')
        transitions[('q6_bisiesto', '1')] = ('q7', '1', 'R')
        transitions[('q6_normal', '0')] = ('q7', '0', 'R')
        transitions[('q6_normal', '1')] = ('q7', '1', 'R')

        # Mes - segundo dígito
        transitions[('q7', '0')] = ('q8_mes30', '0', 'R')
        transitions[('q7', '1')] = ('q8_mes31', '1', 'R')
        transitions[('q7', '2')] = ('q8_feb', '2', 'R')
        transitions[('q7', '3')] = ('q8_mes31', '3', 'R')
        transitions[('q7', '4')] = ('q8_mes30', '4', 'R')
        transitions[('q7', '5')] = ('q8_mes31', '5', 'R')
        transitions[('q7', '6')] = ('q8_mes30', '6', 'R')
        transitions[('q7', '7')] = ('q8_mes31', '7', 'R')
        transitions[('q7', '8')] = ('q8_mes31', '8', 'R')
        transitions[('q7', '9')] = ('q8_mes30', '9', 'R')

        # Días en febrero - primer dígito
        transitions[('q8_feb', '0')] = ('q9_feb0', '0', 'R')
        transitions[('q8_feb', '1')] = ('q9_feb1', '1', 'R')
        transitions[('q8_feb', '2')] = ('q9_feb2', '2', 'R')

        # Días en febrero - segundo dígito para años bisiestos
        if self.current_state == 'q6_bisiesto':
            for i in range(10):
                if i <= 9:  # Permite hasta 29
                    transitions[('q9_feb2', str(i))] = ('q10', str(i), 'R')
        else:  # Años no bisiestos
            for i in range(9):  # Solo hasta 28
                transitions[('q9_feb2', str(i))] = ('q10', str(i), 'R')

        # Días para meses de 31 días
        transitions[('q8_mes31', '0')] = ('q9_dia0', '0', 'R')
        transitions[('q8_mes31', '1')] = ('q9_dia1', '1', 'R')
        transitions[('q8_mes31', '2')] = ('q9_dia2', '2', 'R')
        transitions[('q8_mes31', '3')] = ('q9_dia3', '3', 'R')

        # Días para meses de 30 días
        transitions[('q8_mes30', '0')] = ('q9_dia0', '0', 'R')
        transitions[('q8_mes30', '1')] = ('q9_dia1', '1', 'R')
        transitions[('q8_mes30', '2')] = ('q9_dia2', '2', 'R')
        transitions[('q8_mes30', '3')] = ('q9_dia0', '3', 'R')  # Solo hasta 30

        # Segundo dígito del día
        for i in range(10):
            transitions[('q9_dia0', str(i))] = ('q10', str(i), 'R')
            if i <= 9:
                transitions[('q9_dia1', str(i))] = ('q10', str(i), 'R')
            if i <= 9:
                transitions[('q9_dia2', str(i))] = ('q10', str(i), 'R')
            if i <= 1:  # Para 31
                transitions[('q9_dia3', str(i))] = ('q10', str(i), 'R')

        # Sexo
        transitions[('q10', 'H')] = ('q11', 'H', 'R')
        transitions[('q10', 'M')] = ('q11', 'M', 'R')

       # Estado de nacimiento (primera letra)
        transitions[('q11', 'A')] = ('q12_A', 'A', 'R')  # Aguascalientes
        transitions[('q11', 'B')] = ('q12_B', 'B', 'R')  # Baja California, Baja California Sur
        transitions[('q11', 'C')] = ('q12_C', 'C', 'R')  # Coahuila, Colima, Chiapas, Chihuahua, Campeche
        transitions[('q11', 'D')] = ('q12_D', 'D', 'R')  # Durango, Distrito Federal
        transitions[('q11', 'G')] = ('q12_G', 'G', 'R')  # Guanajuato, Guerrero
        transitions[('q11', 'H')] = ('q12_H', 'H', 'R')  # Hidalgo
        transitions[('q11', 'J')] = ('q12_J', 'J', 'R')  # Jalisco
        transitions[('q11', 'M')] = ('q12_M', 'M', 'R')  # Michoacán, Morelos, México
        transitions[('q11', 'N')] = ('q12_N', 'N', 'R')  # Nayarit, Nuevo León, Nacido en el Extranjero
        transitions[('q11', 'O')] = ('q12_O', 'O', 'R')  # Oaxaca
        transitions[('q11', 'P')] = ('q12_P', 'P', 'R')  # Puebla
        transitions[('q11', 'Q')] = ('q12_Q', 'Q', 'R')  # Querétaro, Quintana Roo
        transitions[('q11', 'S')] = ('q12_S', 'S', 'R')  # San Luis Potosí, Sinaloa, Sonora
        transitions[('q11', 'T')] = ('q12_T', 'T', 'R')  # Tabasco, Tamaulipas, Tlaxcala
        transitions[('q11', 'V')] = ('q12_V', 'V', 'R')  # Veracruz
        transitions[('q11', 'Y')] = ('q12_Y', 'Y', 'R')  # Yucatán
        transitions[('q11', 'Z')] = ('q12_Z', 'Z', 'R')  # Zacatecas

        # Segunda letra del estado (todas las combinaciones válidas)
        transitions[('q12_A', 'S')] = ('q13', 'S', 'R')  # AS - Aguascalientes
        transitions[('q12_B', 'C')] = ('q13', 'C', 'R')  # BC - Baja California
        transitions[('q12_B', 'S')] = ('q13', 'S', 'R')  # BS - Baja California Sur
        transitions[('q12_C', 'L')] = ('q13', 'L', 'R')  # CL - Coahuila
        transitions[('q12_C', 'M')] = ('q13', 'M', 'R')  # CM - Colima
        transitions[('q12_C', 'S')] = ('q13', 'S', 'R')  # CS - Chiapas
        transitions[('q12_C', 'H')] = ('q13', 'H', 'R')  # CH - Chihuahua
        transitions[('q12_C', 'P')] = ('q13', 'P', 'R')  # CP - Campeche
        transitions[('q12_D', 'G')] = ('q13', 'G', 'R')  # DG - Durango
        transitions[('q12_D', 'F')] = ('q13', 'F', 'R')  # DF - Distrito Federal
        transitions[('q12_G', 'T')] = ('q13', 'T', 'R')  # GT - Guanajuato
        transitions[('q12_G', 'R')] = ('q13', 'R', 'R')  # GR - Guerrero
        transitions[('q12_H', 'G')] = ('q13', 'G', 'R')  # HG - Hidalgo
        transitions[('q12_J', 'C')] = ('q13', 'C', 'R')  # JC - Jalisco
        transitions[('q12_M', 'H')] = ('q13', 'H', 'R')  # MH - Michoacán
        transitions[('q12_M', 'S')] = ('q13', 'S', 'R')  # MS - Morelos
        transitions[('q12_M', 'X')] = ('q13', 'X', 'R')  # MX - México
        transitions[('q12_N', 'T')] = ('q13', 'T', 'R')  # NT - Nayarit
        transitions[('q12_N', 'L')] = ('q13', 'L', 'R')  # NL - Nuevo León
        transitions[('q12_N', 'E')] = ('q13', 'E', 'R')  # NE - Nacido en el Extranjero
        transitions[('q12_O', 'C')] = ('q13', 'C', 'R')  # OC - Oaxaca
        transitions[('q12_P', 'L')] = ('q13', 'L', 'R')  # PL - Puebla
        transitions[('q12_Q', 'T')] = ('q13', 'T', 'R')  # QT - Querétaro
        transitions[('q12_Q', 'R')] = ('q13', 'R', 'R')  # QR - Quintana Roo
        transitions[('q12_S', 'P')] = ('q13', 'P', 'R')  # SP - San Luis Potosí
        transitions[('q12_S', 'L')] = ('q13', 'L', 'R')  # SL - Sinaloa
        transitions[('q12_S', 'R')] = ('q13', 'R', 'R')  # SR - Sonora
        transitions[('q12_T', 'C')] = ('q13', 'C', 'R')  # TC - Tabasco
        transitions[('q12_T', 'S')] = ('q13', 'S', 'R')  # TS - Tamaulipas
        transitions[('q12_T', 'L')] = ('q13', 'L', 'R')  # TL - Tlaxcala
        transitions[('q12_V', 'Z')] = ('q13', 'Z', 'R')  # VZ - Veracruz
        transitions[('q12_Y', 'N')] = ('q13', 'N', 'R')  # YN - Yucatán
        transitions[('q12_Z', 'S')] = ('q13', 'S', 'R')  # ZS - Zacatecas

        # Consonantes del primer apellido
        for letra in 'BCDFGHJKLMNPQRSTVWXYZ':
            transitions[('q13', letra)] = ('q14', letra, 'R')
            transitions[('q14', letra)] = ('q15', letra, 'R')

        # Consonante del segundo apellido
        for letra in 'BCDFGHJKLMNPQRSTVWXYZ':
            transitions[('q15', letra)] = ('q16', letra, 'R')

        # Homoclave
        for letra in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            transitions[('q16', letra)] = ('q17', letra, 'R')

        # Homoclave
        for caracter in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            transitions[('q17', caracter)] = ('q18', caracter, 'R')
            transitions[('q18', caracter)] = ('qf', caracter, 'R')

        return transitions
    
    
    def step(self):
        if self.head_position < 0:
            return False
            
        if self.head_position >= len(self.tape):
            self.tape.append('')
            
        current_symbol = self.tape[self.head_position]
        transition_key = (self.current_state, current_symbol)
        
        if transition_key not in self.transitions:
            return False
            
        new_state, write_symbol, movement = self.transitions[transition_key]
        self.tape[self.head_position] = write_symbol
        self.current_state = new_state
        
        if movement == 'R':
            self.head_position += 1
        elif movement == 'L':
            self.head_position -= 1
            
        return True
        
    def run(self, input_string):
        self.tape = list(input_string)
        self.head_position = 0
        self.current_state = 'q0'
        
        while self.step():
            continue
            
        return ''.join(self.tape)


class ModernTuringGUI:
    def __init__(self):
        # Configuración de la ventana principal
        self.root = tk.Tk()
        self.root.title("Máquina de Turing - Validador CURP")
        self.root.geometry("900x600")
        self.root.configure(bg="#2E3B4E")
        
        # Configurar estilo
        self.setup_styles()
        
        # Máquina de Turing
        self.turing_machine = TuringMachine()
        
        # Crear el contenido
        self.create_widgets()
        
    def setup_styles(self):
        # Configurar estilos
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2E3B4E')
        self.style.configure('TLabel', 
                           background='#2E3B4E', 
                           foreground='white',
                           font=('Helvetica', 10))
        self.style.configure('Header.TLabel',
                           background='#2E3B4E',
                           foreground='white',
                           font=('Helvetica', 24, 'bold'))
        self.style.configure('SubHeader.TLabel',
                           background='#2E3B4E',
                           foreground='#B0B9C6',
                           font=('Helvetica', 12))
        self.style.configure('TEntry',
                           fieldbackground='#3E4C63',
                           foreground='white',
                           font=('Helvetica', 12))
        self.style.configure('Run.TButton',
                           background='#4CAF50',
                           foreground='white',
                           padding=(20, 10),
                           font=('Helvetica', 12, 'bold'))
        
    def create_widgets(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.root, style='TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        ttk.Label(self.main_frame,
                 text="Validador de CURP",
                 style='Header.TLabel').pack(pady=(0,5))
        
        ttk.Label(self.main_frame,
                 text="Ingrese la CURP para validar su formato",
                 style='SubHeader.TLabel').pack(pady=(0,20))
        
        # Frame de entrada
        input_frame = ttk.Frame(self.main_frame, style='TFrame')
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Entrada
        self.input_var = tk.StringVar()
        entry = tk.Entry(
            input_frame,
            textvariable=self.input_var,
            font=('Helvetica', 14),
            bg='#3E4C63',
            fg='white',
            insertbackground='white',  # cursor color
            width=40
        )
        entry.pack(side=tk.LEFT, padx=10)
        
        # Botón de validación
        validate_button = tk.Button(
            input_frame,
            text="Validar",
            command=self.run_machine,
            font=('Helvetica', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049',
            activeforeground='white',
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        validate_button.pack(side=tk.LEFT, padx=10)
        
        # Frame para la cinta
        self.tape_frame = ttk.Frame(self.main_frame, style='TFrame')
        self.tape_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        ttk.Label(self.tape_frame,
                 text="Estado de la Cinta",
                 style='SubHeader.TLabel').pack(pady=(0,10))
        
        # Canvas para la cinta
        self.tape_canvas = tk.Canvas(
            self.tape_frame,
            bg='#3E4C63',
            height=100,
            highlightthickness=0
        )
        self.tape_canvas.pack(fill=tk.X, padx=20)
        
        # Estado actual
        self.state_var = tk.StringVar(value="Estado actual: q0")
        self.state_label = ttk.Label(
            self.main_frame,
            textvariable=self.state_var,
            style='TLabel'
        )
        self.state_label.pack(pady=10)
        
        # Mensajes
        self.message_var = tk.StringVar()
        self.message_label = ttk.Label(
            self.main_frame,
            textvariable=self.message_var,
            style='TLabel'
        )
        self.message_label.pack(pady=10)
        
    def update_tape_display(self):
        self.tape_canvas.delete("all")
        
        cell_width = 40
        cell_height = 40
        x_start = 20
        y_start = 30
        
        for i, symbol in enumerate(self.turing_machine.tape):
            x = x_start + (i * cell_width)
            # Color verde para la posición actual del cabezal
            cell_color = "#4CAF50" if i == self.turing_machine.head_position else "#5C6B7F"
            
            # Dibujar celda
            self.tape_canvas.create_rectangle(
                x, y_start,
                x + cell_width, y_start + cell_height,
                fill=cell_color,
                outline="white",
                width=2
            )
            
            # Dibujar símbolo
            self.tape_canvas.create_text(
                x + cell_width/2,
                y_start + cell_height/2,
                text=symbol,
                fill="white",
                font=('TkFixedFont', 12)
            )
    
    def run_machine(self):
        input_string = self.input_var.get().upper()
        if not input_string:
            self.show_error("Por favor ingrese una CURP")
            return
            
        try:
            result = self.turing_machine.run(input_string)
            self.update_tape_display()
            self.state_var.set(f"Estado actual: {self.turing_machine.current_state}")
            
            if self.turing_machine.current_state == 'qf' or self.turing_machine.current_state == 'q18':
                self.show_success("¡CURP válida!")
            else:
                self.show_error("CURP inválida")
                
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
    
    def show_error(self, message):
        self.message_var.set(message)
        self.message_label.configure(foreground="#FF5252")
        
    def show_success(self, message):
        self.message_var.set(message)
        self.message_label.configure(foreground="#4CAF50")

if __name__ == "__main__":
    app = ModernTuringGUI()
    app.root.mainloop()