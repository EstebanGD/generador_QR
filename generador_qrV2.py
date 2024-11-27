import tkinter as tk
from tkinter import messagebox

# Función para convertir texto a binario
def texto_a_binario(texto):
    return ''.join(format(ord(c), '08b') for c in texto)

# Función para obtener el tamaño en binario
def obtener_tam(cadena):
    return format(len(cadena), '08b')

# Función para dibujar patrones predeterminados
def valores_por_defecto(canvas):
    # Cuadrado superior izquierdo
    canvas.create_rectangle(0, 0, 140, 140, fill="black")
    canvas.create_rectangle(20, 20, 120, 120, fill="white")
    canvas.create_rectangle(40, 40, 100, 100, fill="black")

    # Cuadrado inferior izquierdo
    canvas.create_rectangle(0, 360, 140, 500, fill="black")
    canvas.create_rectangle(20, 380, 120, 480, fill="white")
    canvas.create_rectangle(40, 400, 100, 460, fill="black")

    # Cuadrado superior derecho
    canvas.create_rectangle(360, 0, 500, 140, fill="black")
    canvas.create_rectangle(380, 20, 480, 120, fill="white")
    canvas.create_rectangle(400, 40, 460, 100, fill="black")

    # Pixel que siempre es oscuro (alineado con el centro)
    canvas.create_rectangle(160, 340, 180, 360, fill="black")

    # Formato información (área inferior derecha)
    canvas.create_rectangle(480, 480, 500, 500, fill="white")
    canvas.create_rectangle(460, 480, 480, 500, fill="black")
    canvas.create_rectangle(480, 460, 500, 480, fill="white")
    canvas.create_rectangle(460, 460, 480, 480, fill="white")

# Función para dibujar patrones de temporización
def patrones_temporizacion(canvas):
    # Patrón de temporización horizontal
    for i in range(140, 500 - 140, 20):
        color = "black" if ((i // 20) % 2 == 0) else "white"
        canvas.create_rectangle(i, 120, i + 20, 140, fill=color)

    # Patrón de temporización vertical
    for j in range(140, 500 - 140, 20):
        color = "black" if ((j // 20) % 2 == 0) else "white"
        canvas.create_rectangle(120, j, 140, j + 20, fill=color)

# Función para codificar el número de caracteres
def num_caracteres(canvas, x, y, cad):
    # Comenzamos en la posición especificada y colocamos los bits hacia arriba
    for bit in cad:
        color = "white" if bit == '0' else "black"
        canvas.create_rectangle(x, y, x + 20, y + 20, fill=color)
        y -= 20  # Subir en el eje Y
        # Si llegamos al límite superior, movemos a la siguiente columna a la izquierda
        if y < 0:
            y = 500 - 20
            x -= 20  # Mover a la siguiente columna

# Función para codificar la cadena de caracteres
def cadena_cod(canvas, x, y, cad):
    direction = -1  # -1 para arriba, 1 para abajo
    i = 0  # Índice para recorrer la cadena de bits

    while x >= 0 and i < len(cad):
        for _ in range(2):  # Cada columna tiene 2 módulos de ancho
            if i >= len(cad):
                break
            y_start = y
            while 0 <= y < 500 and i < len(cad):
                color = "white" if cad[i] == '0' else "black"
                canvas.create_rectangle(x, y, x + 20, y + 20, fill=color)
                y += direction * 20
                i += 1
            # Cambiar de dirección al final de la columna
            direction *= -1
            y = y_start + direction * 20  # Ajustar posición Y para la nueva columna
            x -= 20  # Mover a la siguiente columna a la izquierda

# Función para generar el QR
def generar_qr():
    mensaje = entry.get()
    if not mensaje:
        messagebox.showwarning("Entrada Vacía", "Por favor, ingresa un mensaje a codificar.")
        return

    # Limpiar el canvas antes de generar un nuevo QR
    canvas.delete("all")

    # Redibujar la cuadrícula
    for i in range(0, 500, 20):
        for j in range(0, 500, 20):
            canvas.create_rectangle(i, j, i + 20, j + 20, fill="white", outline="grey")

    # Dibujar patrones predeterminados y de temporización
    valores_por_defecto(canvas)
    patrones_temporizacion(canvas)

    # Convertir el mensaje a binario
    binario = texto_a_binario(mensaje)
    tam = obtener_tam(mensaje)

    # Codificar el tamaño y el mensaje en el QR
    # Ajustamos las posiciones iniciales para evitar superponer los patrones fijos
    num_caracteres(canvas, 500 - 20, 500 - 20, tam)
    cadena_cod(canvas, 500 - 60, 500 - 160, binario)

# Creación de la pantalla principal
pantalla = tk.Tk()
pantalla.title("Generador QR")
pantalla.geometry("500x550")  # Ajuste de tamaño para incluir el campo de entrada

# Campo de entrada y botón en la parte superior
control_frame = tk.Frame(pantalla)
control_frame.pack(pady=10)

label = tk.Label(control_frame, text="Mensaje a codificar:")
label.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(control_frame, width=30)
entry.pack(side=tk.LEFT, padx=5)

boton = tk.Button(control_frame, text="Generar QR", command=generar_qr)
boton.pack(side=tk.LEFT, padx=5)

# Creación del espacio de dibujo (canvas) debajo
canvas_frame = tk.Frame(pantalla)
canvas_frame.pack()

canvas = tk.Canvas(canvas_frame, width=500, height=500, bg="white")
canvas.pack()

pantalla.mainloop()
