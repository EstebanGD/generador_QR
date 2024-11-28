import numpy as np
from PIL import Image

matrizQr=np.zeros((25,25), dtype=int) #inicializar una matriz 25x25

cadena = input("Ingrese el mensaje a codificar: ")

# Convertimos cada carácter a su representación binaria (8 bits)
fInfo= "0100"
binario = ''.join(format(ord(c), '08b') for c in cadena)
tam = ''.join(format(len(cadena), '08b'))
cadTotal = fInfo + tam + binario

def patrones_fijos_esquinas(matriz,f,c):
    for i in range(7):
        for j in range(7):
            if i == 0 or i == 6:
                matriz[(f+i)%25,(c+j)%25]=3
            elif i == 1 or i==5:
                if j == 0 or j == 6:
                    matriz[(f+i)%25,(c+j)%25]=3
                else:
                    matriz[(f+i)%25,(c+j)%25]=4
            elif i == 2 or i == 4:
                if j == 1 or j == 5:
                    matriz[(f+i)%25,(c+j)%25]=4
                else:
                    matriz[(f+i)%25,(c+j)%25]=3
            else:
                if j == 1 or j == 3 or j == 5:
                    matriz[(f+i)%25,(c+j)%25]=4
                else:
                    matriz[(f+i)%25,(c+j)%25]=3

def patron_fijo_cuadrado(matriz):
    for i in range(5):
        for j in range(5):
            if i == 0 or i == 4:
                matriz[(16+i)%25,(16+j)%25]=3
            elif i == 1 or i==3:
                if j == 0 or j == 4:
                    matriz[(16+i)%25,(16+j)%25]=3
                else:
                    matriz[(16+i)%25,(16+j)%25]=4
            else:
                if j == 1 or j == 3:
                    matriz[(16+i)%25,(16+j)%25]=4
                else:
                    matriz[(16+i)%25,(16+j)%25]=3
    matriz[(17)%25,(8)%25]=3

def patron_temporizacion(matriz,c,dir):
    if dir == 0:
        for j in range(6):
            if j == 0:
                matriz[(6)%25,(c)%25]=3
            else:
                matriz[(6)%25,(c+(j*2))%25]=3
    else:
        for j in range(6):
            if j == 0:
                matriz[(c)%25,(6)%25]=3
            else:
                matriz[(c+(j*2))%25,(6)%25]=3

def espacio_reservado(matriz,f,c,p):
    if p == 1:
        for i in range(2):
            for j in range(9):
                if  matriz[(f+i)%25,(c+j)%25] != 3:
                    matriz[(f+i)%25,(c+j)%25] = 4
    elif p == 2:
        for i in range(2):
            for j in range(9):
                if  matriz[(f+j)%25,(c+i)%25] != 3:
                    matriz[(f+j)%25,(c+i)%25] = 4
    elif p == 3:
        for i in range(7):
            if  matriz[(f+i)%25,(c)%25] != 3:
                matriz[(f+i)%25,(c)%25] = 4
    else:
        for i in range(9):
            if  matriz[(f)%25,(c+i)%25] != 3:
                matriz[(f)%25,(c+i)%25] = 4

def llenado_matriz(matriz,cad):
    pCad=0
    fila=24
    col=24
    dir=1
    count=0

    while pCad < len(cad):
        if matriz[fila,col] == 0 and dir == 1:
            for i in range(2):
                matriz[fila,col-i]=int(cad[pCad])
                pCad+=1
            """if fila < 9:
                fila-=1
                col=22"""
            fila-=1
        else:
            for i in range(2):
                matriz[fila,22-i]=int(cad[pCad])
                pCad+=1
            fila+=1

def save_qr_colored(matriz):
    filename="qr_code_colored.png"
    # Define el mapa de colores
    color_map = {
        0: (255, 255, 255),  # Blanco
        1: (0, 0, 0),        # Negro
        3: (0, 0, 0),      # Verde
        4: (255, 255, 255),      # Azul
    }
    
    # Obtén las dimensiones de la matriz
    height, width = matriz.shape
    
    # Crear una imagen RGB vacía
    img_array = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Mapear los valores de la matriz a los colores
    for value, color in color_map.items():
        img_array[matriz == value] = color  # Asignar el color a los píxeles correspondientes
    
    # Convertir a imagen y guardar
    img = Image.fromarray(img_array)
    img = img.resize((250, 250), Image.NEAREST)  # Redimensionar para mejor visibilidad
    img.save(filename)

#print(matrizQr)
#print(binario)
print(cadTotal)
print(" ")
patrones_fijos_esquinas(matrizQr,0,0)
patrones_fijos_esquinas(matrizQr,18,0)
patrones_fijos_esquinas(matrizQr,0,18)
patron_fijo_cuadrado(matrizQr)
patron_temporizacion(matrizQr,8,0)
patron_temporizacion(matrizQr,8,1)
espacio_reservado(matrizQr,7,0,1)
espacio_reservado(matrizQr,7,17,1)
espacio_reservado(matrizQr,0,7,2)
espacio_reservado(matrizQr,18,7,2)
espacio_reservado(matrizQr,0,17,3)
espacio_reservado(matrizQr,17,0,4)
llenado_matriz(matrizQr,cadTotal)
print(matrizQr)
save_qr_colored(matrizQr)