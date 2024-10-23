import tkinter as tk

#creacion de la pantalla.
pantalla = tk.Tk()
pantalla.title("Generador QR")
pantalla.geometry("500x500")

#Creacion del espacio de dibujo(canvas).
canvas = tk.Canvas(pantalla, width=500, height=500, bg="white")
canvas.pack()

#cuadricula proporcionada por chatgpt, para distinguir con claridad el espacio de trabajo
for i in range(0, 500, 20):
    for j in range(0, 500, 20):
        canvas.create_rectangle(i, j, i + 20, j + 20, fill="white", outline="grey")

def valores_por_defecto():
    #cuadrado superior izquierdo
    canvas.create_rectangle(0, 0, 140, 140, fill="black")
    canvas.create_rectangle(20, 20, 120, 120, fill="white")
    canvas.create_rectangle(40, 40, 100, 100, fill="black")

    #Cuadrado inferior izquierdo
    canvas.create_rectangle(0, 360, 140, 500, fill="black")
    canvas.create_rectangle(20, 380, 120, 480, fill="white")
    canvas.create_rectangle(40, 400, 100, 460, fill="black")

    #cuadrado superior derecho
    canvas.create_rectangle(360, 0, 500, 140, fill="black")
    canvas.create_rectangle(380, 20, 480, 120, fill="white")
    canvas.create_rectangle(400, 40, 460, 100, fill="black")

    #cuadrado inferior derecho
    canvas.create_rectangle(320, 320, 420, 420, fill="black")
    canvas.create_rectangle(340, 340, 400, 400, fill="white")
    canvas.create_rectangle(360, 360, 380, 380, fill="black")

    #pixel que siempre es oscuro
    canvas.create_rectangle(160, 340, 180, 360, fill="black")

    #Formato informacion
    canvas.create_rectangle(480, 480, 500, 500, fill="white")
    canvas.create_rectangle(460, 480, 480, 500, fill="black")
    canvas.create_rectangle(480, 460, 500, 480, fill="white")
    canvas.create_rectangle(460, 460, 480, 480, fill="white")

#patrones de temporizacion
def p_temporizacion_superior():
    x1 = 120
    x2 = 140
    for i in range(11):
        if (i%2 == 0):
            x1 = x1 + 20
            x2 = x2 + 20
            canvas.create_rectangle(x1, 120, x2, 140, fill="white")
        else:
            x1 = x1 + 20
            x2 = x2 + 20
            canvas.create_rectangle(x1, 120, x2, 140, fill="black")

def p_temporizacion_lateral():
    y1 = 120
    y2 = 140
    for i in range(11):
        if (i%2 == 0):
            y1 = y1 + 20
            y2 = y2 + 20
            canvas.create_rectangle(120, y1, 140, y2, fill="white")
        else:
            y1 = y1 + 20
            y2 = y2 + 20
            canvas.create_rectangle(120, y1, 140, y2, fill="black")

# Cadena alfanumérica
cadena = input("Ingrese el mensaje a codificar: ")

# Convertimos cada carácter a su representación binaria (8 bits)
binario = ''.join(format(ord(c), '08b') for c in cadena)
tam = ''.join(format(len(cadena), '08b'))

#codificacion binario cantidad de caracteres
def num_caracteres(x,y,cad):
    aux_x=x
    #aux_y=y
    count = 0

    for c in cad:
        if count <2:
            if c == '0':
                canvas.create_rectangle(x, y, x+20, y+20, fill="white")
                count +=1
                x-=20
            else:
                canvas.create_rectangle(x, y, x+20, y+20, fill="black")
                count +=1
                x-=20
        else:
            count = 0
            x=aux_x
            y=y-20
            if c == '0':
                canvas.create_rectangle(x, y, x+20, y+20, fill="white")
                count +=1
                x-=20
            else:
                canvas.create_rectangle(x, y, x+20, y+20, fill="black")
                count +=1
                x-=20

#codificacion binario cadena de caracteres
def cadena_cod(x,y,cad, band):
    aux_x=x
    x2=440+20
    aux_x2=x2
    x+=20
    count = 0
    for c in cad:
        if y==160:
            band = False
            
        if band == True :
            if count <2:
                x-=20
            else:
                count = 0
                x=aux_x
                y=y-20
                if y==160:
                    x=440
                    y=180
                    if c == '0':
                        canvas.create_rectangle(x, y, x+20, y+20, fill="white")
                        count +=1
                    else:
                        canvas.create_rectangle(x, y, x+20, y+20, fill="black")
                        count +=1
                    band = False
            if c == '0':
                canvas.create_rectangle(x, y, x+20, y+20, fill="white")
                count +=1
            else:
                canvas.create_rectangle(x, y, x+20, y+20, fill="black")
                count +=1
        else:
            y=200
            print(c)
            aux_x2=x2-20
            if count <2:
                x2-=20
            else:
                count = 0
                x2=aux_x2
                y=y+20
            if c == '0':
                canvas.create_rectangle(x2, y, x2+20, y+20, fill="white")
                count +=1
            else:
                canvas.create_rectangle(x2, y, x2+20, y+20, fill="black")
                count +=1

#llamado de funciones
valores_por_defecto()
p_temporizacion_superior()
p_temporizacion_lateral()
num_caracteres(480, 440, tam)
cadena_cod(480, 360, binario, True)

pantalla.mainloop()