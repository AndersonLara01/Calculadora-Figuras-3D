#Librerias requeridas por el código
import tkinter as tk
from abc import ABC, abstractmethod
from math import pi

#Clase abstracta con metodos abstractos para la base de figuras 3D
class Figura3D(ABC):
    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_area_superficial(self, factor_escala = None):
        pass

    @abstractmethod
    def dibujar(self):
        pass

    def obtener_resultado(self, factor_escala=None):
        area_figura = self.calcular_area_superficial(factor_escala)
        return (f"{self.dibujar()}\n"
        f"Volumen: {self.calcular_volumen():.2f}\n"
        f"Área superficial: {area_figura:.2f}")

class Cubo(Figura3D):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        return self.lado ** 3

    def calcular_area_superficial(self, factor_escala = None):
        area_figura = self.lado ** 2 * 6
        if factor_escala is not None:
            area_figura *= factor_escala ** 2
        return area_figura

    def dibujar(self):
        return f"Cubo con lado {self.lado}"

class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return ((4 * (self.radio ** 3)) * pi) /3

    def calcular_area_superficial(self, factor_escala = None):
        area_figura = 4 * pi * self.radio ** 2
        if factor_escala is not None:
            area_figura *= factor_escala ** 2
        return area_figura
    
    def dibujar(self):
        return f"Esfera con radio {self.radio}"

class Cilindro(Figura3D):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return pi * self.radio ** 2 * self.altura

    def calcular_area_superficial(self, factor_escala = None):
        area_figura = (2 * pi * self.radio ** 2) + (2 * pi * self.radio * self.altura)
        if factor_escala is not None:
            area_figura *= factor_escala ** 2
        return area_figura
    def dibujar(self):
        return f"Cilindro con radio {self.radio} y altura {self.altura}"

class Inicio:
    def __init__(self):
        self.figuras = []
        self.ventana = tk.Tk()
        self.ventana.geometry("600x600+470+80")
        self.ventana.title("Calculadora de Figuras 3D")
        self.ventana.resizable(False, False)

        self.title = tk.Label(self.ventana, text="Seleccione la figura que desea calcular", font=("Bright Sunlist", 24), bg="#AAAAAA")
        self.title.pack(side="top", fill="both")

        color_fondo = "#362486"

        self.frame = tk.Frame(self.ventana, bg=color_fondo)
        self.frame.pack(fill="both", expand=True)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        color_botones = "#00E96E"

        self.cubo = tk.Button(self.frame, text="Cubo", font=("Bright Sunlist", 20), background=color_botones, command=self.abrir_ventana_cubo)
        self.cubo.grid(row=0, column=0, padx=20, pady=20)

        self.esfera = tk.Button(self.frame, text="Esfera", font=("Bright Sunlist", 20), background=color_botones, command=self.abrir_ventana_esfera)
        self.esfera.grid(row=0, column=1, padx=20, pady=20)

        self.cilindro = tk.Button(self.frame, text="Cilindro", font=("Bright Sunlist", 20), background=color_botones, command=self.abrir_ventana_cilindro)
        self.cilindro.grid(row=1, column=0, padx=20, pady=20)

        self.nueva_figura = tk.Button(self.frame, text="Proximamente...", font=("Bright Sunlist", 20), background=color_botones)
        self.nueva_figura.grid(row=1, column=1, padx=20, pady=20)

        self.ventana.mainloop()

    def abrir_ventana_cubo(self):
        ventana_cubo = tk.Toplevel(self.ventana)
        ventana_cubo.title("Cálculo de cubo")
        ventana_cubo.geometry("350x320")
        ventana_cubo.resizable(False, False)

        tk.Label(ventana_cubo, text="Lado del cubo:").pack(pady=(15, 0))
        entrada_lado = tk.Entry(ventana_cubo)
        entrada_lado.pack()

        tk.Label(ventana_cubo, text="Factor de escala (opcional):").pack(pady=(10, 0))
        entrada_factor = tk.Entry(ventana_cubo)
        entrada_factor.pack()

        resultado = tk.Label(ventana_cubo, text="", justify="left", wraplength=320)
        resultado.pack(padx=10, pady=15)

        tk.Button(ventana_cubo, text="Calcular", command=lambda: self.calcular_cubo(entrada_lado, entrada_factor, resultado)).pack()

    def calcular_cubo(self, entrada_lado, entrada_factor, resultado):
        try:
            lado = float(entrada_lado.get())
            valor_factor = entrada_factor.get().strip()
            factor_escala = float(valor_factor) if valor_factor else None

            if lado <= 0 or (factor_escala is not None and factor_escala <= 0):
                raise ValueError
        except ValueError:
            resultado.config(text="Ingresa un lado positivo y, si usas factor, un factor positivo.")
            return

        figura = Cubo(lado)
        self.figuras.append(figura)
        resultado.config(text=figura.obtener_resultado(factor_escala))

    def abrir_ventana_esfera(self):
        ventana_esfera = tk.Toplevel(self.ventana)
        ventana_esfera.title("Cálculo de la esfera")
        ventana_esfera.geometry("350x320")
        ventana_esfera.resizable(False, False)        

        tk.Label(ventana_esfera, text="Radio de la esfera:").pack(pady=(15, 0))
        entrada_radio = tk.Entry(ventana_esfera)
        entrada_radio.pack()

        tk.Label(ventana_esfera, text="Factor de escala (opcional):").pack(pady=(10, 0))
        entrada_factor = tk.Entry(ventana_esfera)
        entrada_factor.pack()

        resultado = tk.Label(ventana_esfera, text="", justify="left", wraplength=320)
        resultado.pack(padx=10, pady=15)

        tk.Button(ventana_esfera, text="Calcular", command=lambda: self.calcular_esfera(entrada_radio, entrada_factor, resultado)).pack()  

    def calcular_esfera(self, entrada_radio, entrada_factor, resultado):
        try:
            radio = float(entrada_radio.get())
            valor_factor = entrada_factor.get().strip()
            factor_escala = float(valor_factor) if valor_factor else None

            if radio <= 0 or (factor_escala is not None and factor_escala <= 0):
                raise ValueError
        except ValueError:
            resultado.config(text="Ingresa un radio positivo y, si usas factor, un factor positivo.")
            return        

        figura = Esfera(radio)
        self.figuras.append(figura)
        resultado.config(text=figura.obtener_resultado(factor_escala))

    def abrir_ventana_cilindro(self):
        ventana_cilindro = tk.Toplevel(self.ventana)
        ventana_cilindro.title("Cálculo del cilindro")
        ventana_cilindro.geometry("350x320")
        ventana_cilindro.resizable(False, False)

        tk.Label(ventana_cilindro, text="Radio del cilindro:").pack(pady=(15, 0))
        entrada_radio = tk.Entry(ventana_cilindro)
        entrada_radio.pack()

        tk.Label(ventana_cilindro, text="Altura del cilindro:").pack(pady=(10, 0))
        entrada_altura = tk.Entry(ventana_cilindro)
        entrada_altura.pack()

        tk.Label(ventana_cilindro, text="Factor de escala (opcional):").pack(pady=(5, 0))
        entrada_factor = tk.Entry(ventana_cilindro)
        entrada_factor.pack()

        resultado = tk.Label(ventana_cilindro, text="", justify="left", wraplength=320)
        resultado.pack(padx=10, pady=15)

        tk.Button(ventana_cilindro, text="Calcular", command=lambda: self.calcular_cilindro(entrada_radio, entrada_altura, entrada_factor, resultado)).pack()  

    def calcular_cilindro(self, entrada_radio, entrada_altura, entrada_factor, resultado):
        try:
            radio = float(entrada_radio.get())
            altura = float(entrada_altura.get())
            valor_factor = entrada_factor.get().strip()
            factor_escala = float(valor_factor) if valor_factor else None

            if radio <= 0 or altura <= 0 or (factor_escala is not None and factor_escala <= 0):
                raise ValueError
        except ValueError:
            resultado.config(text="Ingresa un radio positivo y, si usas factor, un factor positivo.")
            return        

        figura = Cilindro(radio, altura)
        self.figuras.append(figura)
        resultado.config(text=figura.obtener_resultado(factor_escala))

if __name__ == "__main__":
    Inicio()