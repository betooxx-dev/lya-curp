import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
from datetime import datetime

class CURPGenerator:
   def __init__(self):
       self.tape = []
       self.head_position = 0
       self.current_state = 'q0'
       
   def validate_fecha(self, dia, mes, año):
       try:
           if not (1 <= mes <= 12):
               return False
               
           dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
           
           if mes == 2 and (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
               dias_por_mes[1] = 29
               
           if not (1 <= dia <= dias_por_mes[mes-1]):
               return False
               
           año_actual = datetime.now().year
           if not (1900 <= año <= año_actual):
               return False
               
           return True
           
       except:
           return False
       
   def generate_curp(self, apellido1, apellido2, nombre, dia, mes, año, sexo, estado):
       if not self.validate_fecha(dia, mes, año):
           raise ValueError("Fecha de nacimiento inválida")
           
       if not apellido1 or not nombre:
           raise ValueError("El primer apellido y nombre son obligatorios")
           
       curp = apellido1[0].upper()
       vocales = 'AEIOU'
       vocal_found = False
       for letra in apellido1[1:]:
           if letra.upper() in vocales:
               curp += letra.upper()
               vocal_found = True
               break
       if not vocal_found:
           curp += 'X'
               
       curp += apellido2[0].upper() if apellido2 else 'X'
       curp += nombre[0].upper()
       
       curp += f"{str(año)[-2:]}{mes:02d}{dia:02d}"
       curp += sexo.upper()
       
       estados = {
           'AGUASCALIENTES': 'AS', 'BAJA CALIFORNIA': 'BC', 
           'BAJA CALIFORNIA SUR': 'BS', 'CAMPECHE': 'CC',
           'COAHUILA': 'CL', 'COLIMA': 'CM',
           'CHIAPAS': 'CS', 'CHIHUAHUA': 'CH',
           'DISTRITO FEDERAL': 'DF', 'DURANGO': 'DG',
           'GUANAJUATO': 'GT', 'GUERRERO': 'GR',
           'HIDALGO': 'HG', 'JALISCO': 'JC',
           'MEXICO': 'MC', 'MICHOACAN': 'MN',
           'MORELOS': 'MS', 'NAYARIT': 'NT',
           'NUEVO LEON': 'NL', 'OAXACA': 'OC',
           'PUEBLA': 'PL', 'QUERETARO': 'QT',
           'QUINTANA ROO': 'QR', 'SAN LUIS POTOSI': 'SP',
           'SINALOA': 'SL', 'SONORA': 'SR',
           'TABASCO': 'TC', 'TAMAULIPAS': 'TS',
           'TLAXCALA': 'TL', 'VERACRUZ': 'VZ',
           'YUCATAN': 'YN', 'ZACATECAS': 'ZS',
           'NACIDO EXTRANJERO': 'NE'
       }
       
       if estado not in estados:
           raise ValueError("Estado inválido")
           
       curp += estados[estado.upper()]
       
       consonantes = 'BCDFGHJKLMNPQRSTVWXYZ'
       consonante_found = False
       for letra in apellido1[1:]:
           if letra.upper() in consonantes:
               curp += letra.upper()
               consonante_found = True
               break
       if not consonante_found:
           curp += 'X'
               
       consonante_found = False
       if apellido2:
           for letra in apellido2[1:]:
               if letra.upper() in consonantes:
                   curp += letra.upper()
                   consonante_found = True
                   break
       if not consonante_found:
           curp += 'X'
               
       consonante_found = False
       for letra in nombre[1:]:
           if letra.upper() in consonantes:
               curp += letra.upper()
               consonante_found = True
               break
       if not consonante_found:
           curp += 'X'
       
       caracteres = string.ascii_uppercase + string.digits
       curp += ''.join(random.choice(caracteres) for _ in range(2))
       
       return curp

class ModernCURPGeneratorGUI:
   def __init__(self):
       self.root = tk.Tk()
       self.root.title("Generador de CURP")
       self.root.geometry("1000x800")
       self.root.configure(bg="#2E3B4E")
       self.setup_styles()
       self.generator = CURPGenerator()
       self.create_widgets()
       
   def setup_styles(self):
       self.style = ttk.Style()
       self.style.theme_use('clam')
       self.style.configure('TFrame', background='#2E3B4E')
       self.style.configure('TLabel', 
                          background='#2E3B4E', 
                          foreground='white',
                          font=('Helvetica', 12))
       self.style.configure('TEntry', 
                          fieldbackground='#3E4C63',
                          foreground='white',
                          font=('Helvetica', 12))
       self.style.configure('Header.TLabel',
                          font=('Helvetica', 28, 'bold'),
                          foreground='#4CAF50')
       self.style.configure('TButton',
                          font=('Helvetica', 12),
                          padding=10)
       
   def create_widgets(self):
       main_frame = ttk.Frame(self.root)
       main_frame.pack(padx=40, pady=40, fill=tk.BOTH, expand=True)
       
       header_frame = ttk.Frame(main_frame)
       header_frame.pack(fill=tk.X, pady=(0,30))
       ttk.Label(header_frame, 
                text="🆔 Generador de CURP",
                style='Header.TLabel').pack()
       
       fields_frame = ttk.Frame(main_frame)
       fields_frame.pack(fill=tk.BOTH, expand=True)
       
       left_frame = ttk.Frame(fields_frame)
       left_frame.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
       
       self.apellido1_var = tk.StringVar()
       self.apellido2_var = tk.StringVar()
       self.nombre_var = tk.StringVar()
       
       name_fields = [
           ("Primer Apellido*:", self.apellido1_var),
           ("Segundo Apellido:", self.apellido2_var),
           ("Nombre(s)*:", self.nombre_var),
       ]
       
       for label, var in name_fields:
           frame = ttk.Frame(left_frame)
           frame.pack(fill=tk.X, pady=10)
           ttk.Label(frame, text=label).pack(anchor=tk.W)
           entry = ttk.Entry(frame, 
                           textvariable=var,
                           font=('Helvetica', 12),
                           width=30)
           entry.pack(fill=tk.X, pady=(5,0))
       
       right_frame = ttk.Frame(fields_frame)
       right_frame.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
       
       fecha_frame = ttk.Frame(right_frame)
       fecha_frame.pack(fill=tk.X, pady=10)
       ttk.Label(fecha_frame, text="Fecha de Nacimiento*:").pack(anchor=tk.W)
       
       fecha_inputs = ttk.Frame(fecha_frame)
       fecha_inputs.pack(fill=tk.X, pady=(5,0))
       
       self.dia_var = tk.StringVar()
       self.mes_var = tk.StringVar()
       self.año_var = tk.StringVar()
       
       ttk.Label(fecha_inputs, text="Día:").pack(side=tk.LEFT)
       ttk.Entry(fecha_inputs, textvariable=self.dia_var, width=3).pack(side=tk.LEFT, padx=2)
       ttk.Label(fecha_inputs, text="Mes:").pack(side=tk.LEFT, padx=(10,0))
       ttk.Entry(fecha_inputs, textvariable=self.mes_var, width=3).pack(side=tk.LEFT, padx=2)
       ttk.Label(fecha_inputs, text="Año:").pack(side=tk.LEFT, padx=(10,0))
       ttk.Entry(fecha_inputs, textvariable=self.año_var, width=5).pack(side=tk.LEFT, padx=2)
       
       sexo_frame = ttk.Frame(right_frame)
       sexo_frame.pack(fill=tk.X, pady=20)
       ttk.Label(sexo_frame, text="Sexo*:").pack(anchor=tk.W)
       
       self.sexo_var = tk.StringVar(value="H")
       sex_buttons_frame = ttk.Frame(sexo_frame)
       sex_buttons_frame.pack(fill=tk.X, pady=(5,0))
       
       def config_sex_button(button, value):
           if self.sexo_var.get() == value:
               button.configure(style='Selected.TButton')
           else:
               button.configure(style='TButton')
               
       self.style.configure('Selected.TButton',
                          background='#4CAF50',
                          font=('Helvetica', 12, 'bold'))
       
       hombre_btn = ttk.Button(sex_buttons_frame,
                             text="👨 Hombre",
                             command=lambda: [self.sexo_var.set("H"), 
                                            config_sex_button(hombre_btn, "H"),
                                            config_sex_button(mujer_btn, "M")])
       hombre_btn.pack(side=tk.LEFT, padx=(0,10))
       
       mujer_btn = ttk.Button(sex_buttons_frame,
                            text="👩 Mujer",
                            command=lambda: [self.sexo_var.set("M"),
                                           config_sex_button(hombre_btn, "H"),
                                           config_sex_button(mujer_btn, "M")])
       mujer_btn.pack(side=tk.LEFT)
       
       estado_frame = ttk.Frame(right_frame)
       estado_frame.pack(fill=tk.X, pady=10)
       ttk.Label(estado_frame, text="Estado*:").pack(anchor=tk.W)
       
       self.estado_var = tk.StringVar()
       estados = ['AGUASCALIENTES', 'BAJA CALIFORNIA', 'BAJA CALIFORNIA SUR', 'CAMPECHE',
                 'COAHUILA', 'COLIMA', 'CHIAPAS', 'CHIHUAHUA', 'DISTRITO FEDERAL', 
                 'DURANGO', 'GUANAJUATO', 'GUERRERO', 'HIDALGO', 'JALISCO', 'MEXICO',
                 'MICHOACAN', 'MORELOS', 'NAYARIT', 'NUEVO LEON', 'OAXACA', 'PUEBLA',
                 'QUERETARO', 'QUINTANA ROO', 'SAN LUIS POTOSI', 'SINALOA', 'SONORA',
                 'TABASCO', 'TAMAULIPAS', 'TLAXCALA', 'VERACRUZ', 'YUCATAN', 'ZACATECAS',
                 'NACIDO EXTRANJERO']
       
       estado_combo = ttk.Combobox(estado_frame, 
                                 textvariable=self.estado_var,
                                 values=estados,
                                 font=('Helvetica', 12),
                                 state='readonly')
       estado_combo.pack(fill=tk.X, pady=(5,0))
       
       ttk.Label(main_frame, 
                text="* Campos obligatorios",
                font=('Helvetica', 10, 'italic')).pack(pady=(10,0))
       
       generate_frame = ttk.Frame(main_frame)
       generate_frame.pack(fill=tk.X, pady=30)
       
       generate_btn = tk.Button(generate_frame,
                              text="Generar CURP",
                              command=self.generate_curp,
                              font=('Helvetica', 14, 'bold'),
                              bg='#4CAF50',
                              fg='white',
                              activebackground='#45a049',
                              activeforeground='white',
                              relief=tk.FLAT,
                              padx=30,
                              pady=15)
       generate_btn.pack()
       
       result_frame = ttk.Frame(main_frame)
       result_frame.pack(fill=tk.X, pady=20)
       
       self.result_var = tk.StringVar()
       result_label = ttk.Label(result_frame,
                              textvariable=self.result_var,
                              font=('Courier', 24, 'bold'),
                              foreground='#4CAF50')
       result_label.pack()
       
   def generate_curp(self):
       try:
           curp = self.generator.generate_curp(
               self.apellido1_var.get(),
               self.apellido2_var.get(),
               self.nombre_var.get(),
               int(self.dia_var.get()),
               int(self.mes_var.get()),
               int(self.año_var.get()),
               self.sexo_var.get(),
               self.estado_var.get()
           )
           self.result_var.set(curp)
       except ValueError as e:
           messagebox.showerror("Error", str(e))
       except Exception as e:
           messagebox.showerror("Error", "Por favor verifica todos los campos")

if __name__ == "__main__":
   app = ModernCURPGeneratorGUI()
   app.root.mainloop()