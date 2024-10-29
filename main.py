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

        # Estado q0 - Transiciones iniciales para todas las letras
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            transitions[('q0', letter)] = ('q1', letter, 'R')

        # Estado q1 - Transiciones para vocales
        for vowel in 'AEIOU':
            transitions[('q1', vowel)] = ('q2', vowel, 'R')

        # Estado q2 - Transiciones para todas las letras
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            transitions[('q2', letter)] = ('q3', letter, 'R')

        # Estado q3 - Transiciones para todas las letras
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            transitions[('q3', letter)] = ('q5', letter, 'R')

        # Estado q5 - Transiciones para dígitos
        transitions[('q5', '0')] = ('q17', '0', 'R')
        transitions[('q5', '1')] = ('q6', '1', 'R')
        transitions[('q5', '2')] = ('q7', '2', 'R')
        transitions[('q5', '3')] = ('q8', '3', 'R')
        transitions[('q5', '4')] = ('q9', '4', 'R')
        transitions[('q5', '5')] = ('q10', '5', 'R')
        transitions[('q5', '6')] = ('q11', '6', 'R')
        transitions[('q5', '7')] = ('q12', '7', 'R')
        transitions[('q5', '8')] = ('q13', '8', 'R')
        transitions[('q5', '9')] = ('q14', '9', 'R')

        # Estado q6 a q14 - Transiciones para el segundo dígito del año
        for state in range(6, 15):
            transitions[(f'q{state}', '2')] = ('q15', '2', 'R')
            transitions[(f'q{state}', '6')] = ('q15', '6', 'R')
            for sym in '013456789':
                transitions[(f'q{state}', sym)] = ('q16', sym, 'R')

        # Estado q15 - Transiciones para el primer dígito del mes
        transitions[('q15', '0')] = ('q18', '0', 'R')
        for sym in '123456789':
            transitions[('q15', sym)] = ('q19', sym, 'R')

        # Estado q16 - Transiciones
        transitions[('q16', '0')] = ('q4', '0', 'R')
        transitions[('q16', '1')] = ('q20', '1', 'R')

        # Estado q17 - Transiciones
        transitions[('q17', '0')] = ('q15', '0', 'R')
        transitions[('q17', '4')] = ('q15', '4', 'R')
        transitions[('q17', '8')] = ('q15', '8', 'R')
        for sym in '123567':
            transitions[('q17', sym)] = ('q16', sym, 'R')

        # Estado q4 - Transiciones completas
        transitions[('q4', '0')] = ('q35', '0', 'R')
        transitions[('q4', '1')] = ('q35', '1', 'R')
        transitions[('q4', '2')] = ('q33', '2', 'R')
        transitions[('q4', '4')] = ('q34', '4', 'R')
        transitions[('q4', '6')] = ('q34', '6', 'R')
        transitions[('q4', '9')] = ('q34', '9', 'R')
        transitions[('q4', '3')] = ('q35', '3', 'R')
        transitions[('q4', '5')] = ('q35', '5', 'R')
        transitions[('q4', '7')] = ('q35', '7', 'R')
        transitions[('q4', '8')] = ('q35', '8', 'R')

        # Estado q18 - Transiciones
        transitions[('q18', '2')] = ('q23', '2', 'R')
        transitions[('q18', '4')] = ('q22', '4', 'R')
        transitions[('q18', '6')] = ('q22', '6', 'R')
        transitions[('q18', '9')] = ('q22', '9', 'R')
        for sym in '13578':
            transitions[('q18', sym)] = ('q21', sym, 'R')

        # Estado q19 - Transiciones
        transitions[('q19', '0')] = ('q21', '0', 'R')
        transitions[('q19', '1')] = ('q22', '1', 'R')
        transitions[('q19', '2')] = ('q21', '2', 'R')
        transitions[('q19', '9')] = ('q21', '9', 'R')

        # Estado q20 - Transiciones
        transitions[('q20', '0')] = ('q35', '0', 'R')
        transitions[('q20', '2')] = ('q35', '2', 'R')

        # Estado q21 - Transiciones
        transitions[('q21', '0')] = ('q30', '0', 'R')
        transitions[('q21', '1')] = ('q31', '1', 'R')
        transitions[('q21', '2')] = ('q31', '2', 'R')
        transitions[('q21', '3')] = ('q32', '3', 'R')

        # Estado q22 - Transiciones
        transitions[('q22', '0')] = ('q27', '0', 'R')
        transitions[('q22', '1')] = ('q28', '1', 'R')
        transitions[('q22', '2')] = ('q28', '2', 'R')
        transitions[('q22', '3')] = ('q29', '3', 'R')

        # Estado q23 - Transiciones
        transitions[('q23', '0')] = ('q24', '0', 'R')
        transitions[('q23', '1')] = ('q26', '1', 'R')
        transitions[('q23', '2')] = ('q26', '2', 'R')

        # Estados q24 a q34 - Transiciones a q25
        for sym in '0123456789':
            transitions[('q24', sym)] = ('q25', sym, 'R')
            transitions[('q26', sym)] = ('q25', sym, 'R')
            transitions[('q27', sym)] = ('q25', sym, 'R')
            transitions[('q28', sym)] = ('q25', sym, 'R')
            transitions[('q29', sym)] = ('q25', sym, 'R')
            transitions[('q30', sym)] = ('q25', sym, 'R')
            transitions[('q31', sym)] = ('q25', sym, 'R')
            transitions[('q32', sym)] = ('q25', sym, 'R')

        # Estado q33 - Transiciones
        transitions[('q33', '0')] = ('q36', '0', 'R')
        transitions[('q33', '1')] = ('q37', '1', 'R')
        transitions[('q33', '2')] = ('q37', '2', 'R')

        # Estado q34 - Transiciones
        transitions[('q34', '0')] = ('q39', '0', 'R')
        transitions[('q34', '1')] = ('q40', '1', 'R')
        transitions[('q34', '2')] = ('q40', '2', 'R')
        transitions[('q34', '3')] = ('q41', '3', 'R')

        # Estado q35 - Transiciones
        transitions[('q35', '0')] = ('q42', '0', 'R')
        transitions[('q35', '1')] = ('q43', '1', 'R')
        transitions[('q35', '2')] = ('q43', '2', 'R')
        transitions[('q35', '3')] = ('q44', '3', 'R')

        # Estados q36 a q44 - Transiciones a q38
        for sym in '0123456789':
            transitions[('q36', sym)] = ('q38', sym, 'R')
            transitions[('q37', sym)] = ('q38', sym, 'R')
            transitions[('q39', sym)] = ('q38', sym, 'R')
            transitions[('q40', sym)] = ('q38', sym, 'R')
            transitions[('q41', sym)] = ('q38', sym, 'R')
            transitions[('q42', sym)] = ('q38', sym, 'R')
            transitions[('q43', sym)] = ('q38', sym, 'R')
            transitions[('q44', sym)] = ('q38', sym, 'R')

        # Estado q25 - Transiciones
        transitions[('q25', 'H')] = ('q45', 'H', 'R')
        transitions[('q25', 'M')] = ('q45', 'M', 'R')

        # Estado q38 - Transiciones
        transitions[('q38', 'H')] = ('q45', 'H', 'R')
        transitions[('q38', 'M')] = ('q45', 'M', 'R')

        # Estado q45 - Primera letra de la entidad federativa
        transitions[('q45', 'A')] = ('q46', 'A', 'R')  # AS
        transitions[('q45', 'B')] = ('q47', 'B', 'R')  # BC, BS
        transitions[('q45', 'C')] = ('q48', 'C', 'R')  # CC, CL, CM, CS, CH
        transitions[('q45', 'D')] = ('q49', 'D', 'R')  # DF, DG
        transitions[('q45', 'G')] = ('q50', 'G', 'R')  # GT, GR
        transitions[('q45', 'H')] = ('q51', 'H', 'R')  # HG
        transitions[('q45', 'J')] = ('q52', 'J', 'R')  # JC
        transitions[('q45', 'M')] = ('q53', 'M', 'R')  # MC, MN, MS
        transitions[('q45', 'N')] = ('q54', 'N', 'R')  # NT, NL, NE
        transitions[('q45', 'O')] = ('q55', 'O', 'R')  # OC
        transitions[('q45', 'P')] = ('q56', 'P', 'R')  # PL
        transitions[('q45', 'Q')] = ('q57', 'Q', 'R')  # QT, QR
        transitions[('q45', 'S')] = ('q58', 'S', 'R')  # SP, SL, SR
        transitions[('q45', 'T')] = ('q59', 'T', 'R')  # TC, TS, TL
        transitions[('q45', 'V')] = ('q60', 'V', 'R')  # VZ
        transitions[('q45', 'Y')] = ('q61', 'Y', 'R')  # YN
        transitions[('q45', 'Z')] = ('q62', 'Z', 'R')  # ZS

        # Transiciones específicas para cada estado según la segunda letra permitida
        # Estado q46 (A-)
        transitions[('q46', 'S')] = ('q63', 'S', 'R')  # AS - Aguascalientes

        # Estado q47 (B-)
        transitions[('q47', 'C')] = ('q63', 'C', 'R')  # BC - Baja California
        transitions[('q47', 'S')] = ('q63', 'S', 'R')  # BS - Baja California Sur

        # Estado q48 (C-)
        transitions[('q48', 'C')] = ('q63', 'C', 'R')  # CC - Campeche
        transitions[('q48', 'L')] = ('q63', 'L', 'R')  # CL - Coahuila
        transitions[('q48', 'M')] = ('q63', 'M', 'R')  # CM - Colima
        transitions[('q48', 'S')] = ('q63', 'S', 'R')  # CS - Chiapas
        transitions[('q48', 'H')] = ('q63', 'H', 'R')  # CH - Chihuahua

        # Estado q49 (D-)
        transitions[('q49', 'F')] = ('q63', 'F', 'R')  # DF - Ciudad de México
        transitions[('q49', 'G')] = ('q63', 'G', 'R')  # DG - Durango

        # Estado q50 (G-)
        transitions[('q50', 'T')] = ('q63', 'T', 'R')  # GT - Guanajuato
        transitions[('q50', 'R')] = ('q63', 'R', 'R')  # GR - Guerrero

        # Estado q51 (H-)
        transitions[('q51', 'G')] = ('q63', 'G', 'R')  # HG - Hidalgo

        # Estado q52 (J-)
        transitions[('q52', 'C')] = ('q63', 'C', 'R')  # JC - Jalisco

        # Estado q53 (M-)
        transitions[('q53', 'C')] = ('q63', 'C', 'R')  # MC - Estado de México
        transitions[('q53', 'N')] = ('q63', 'N', 'R')  # MN - Michoacán
        transitions[('q53', 'S')] = ('q63', 'S', 'R')  # MS - Morelos

        # Estado q54 (N-)
        transitions[('q54', 'T')] = ('q63', 'T', 'R')  # NT - Nayarit
        transitions[('q54', 'L')] = ('q63', 'L', 'R')  # NL - Nuevo León
        transitions[('q54', 'E')] = ('q63', 'E', 'R')  # NE - Nacido en el Extranjero

        # Estado q55 (O-)
        transitions[('q55', 'C')] = ('q63', 'C', 'R')  # OC - Oaxaca

        # Estado q56 (P-)
        transitions[('q56', 'L')] = ('q63', 'L', 'R')  # PL - Puebla

        # Estado q57 (Q-)
        transitions[('q57', 'T')] = ('q63', 'T', 'R')  # QT - Querétaro
        transitions[('q57', 'R')] = ('q63', 'R', 'R')  # QR - Quintana Roo

        # Estado q58 (S-)
        transitions[('q58', 'P')] = ('q63', 'P', 'R')  # SP - San Luis Potosí
        transitions[('q58', 'L')] = ('q63', 'L', 'R')  # SL - Sinaloa
        transitions[('q58', 'R')] = ('q63', 'R', 'R')  # SR - Sonora

        # Estado q59 (T-)
        transitions[('q59', 'C')] = ('q63', 'C', 'R')  # TC - Tabasco
        transitions[('q59', 'S')] = ('q63', 'S', 'R')  # TS - Tamaulipas
        transitions[('q59', 'L')] = ('q63', 'L', 'R')  # TL - Tlaxcala

        # Estado q60 (V-)
        transitions[('q60', 'Z')] = ('q63', 'Z', 'R')  # VZ - Veracruz

        # Estado q61 (Y-)
        transitions[('q61', 'N')] = ('q63', 'N', 'R')  # YN - Yucatán

        # Estado q62 (Z-)
        transitions[('q62', 'S')] = ('q63', 'S', 'R')  # ZS - Zacatecas

        # Estados q63 a q68 - Transiciones en cadena para el resto de la CURP
        for state, next_state in [(63, 64), (64, 65), (65, 66), (66, 67), (67, 68)]:
            for sym in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                transitions[(f'q{state}', sym)] = (f'q{next_state}', sym, 'R')

        # Estado final
        transitions[('q68', '')] = ('q69', '', 'S')

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
            
            if self.turing_machine.current_state == 'q69':
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