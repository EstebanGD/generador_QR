import numpy as np
from PIL import Image

def crear_qr_conmatriz():
    
    #Crear una matriz inicializada en blanco (1).
    
    return np.ones((25, 25), dtype=int)  # 1 es blanco, 0 será negro


def insertar_mensaje(matriz, mensaje_binario):
    
    #Inserta el mensaje binario en la matriz del QR, incluyendo el modo y la longitud del mensaje.

    #global fila_final #Llamamos las variables globales
    #global col_final

    # Modo: 0100 (4 bits para binario)
    modo = '0100'
    # Terminadores: indican el final del mensaje
    terminadores = "0000"

    # Tamaño del mensaje en bits (8 bits en binario)
    longitud_mensaje = bin(len(mensaje_binario) // 8)[2:]
    longitud_mensaje = longitud_mensaje.zfill(8)
    
    size = matriz.shape[0]
    
    """if fila_final == None:"""
    col = size - 1  # Comienza desde la última columna 24
    fila = size - 1  # Comienza desde la última fila 24
        # Combinar modo, longitud y mensaje
    datos = modo + longitud_mensaje + mensaje_binario + terminadores
        #datos = datos + calcular_relleno_binario(datos)
    """else:
        #Inicia a insertarse en donde termino el mensaje
        #col = col_final
        #fila = fila_final 
        datos = mensaje_binario #Este es el codigo de correccion de errores"""

    direction = -1  # Zigzag (-1: hacia arriba, 1: hacia abajo)
    datos_index = 0  # Índice actual en los datos
    cambio = 0 # Para saber cuando cambiar la fila 
    topeArriba = 0 # para saber cuando cambiar el sentido
    topeAbajo = 2
    while datos_index < len(datos) and col >= 0:
        # Ignorar áreas reservadas
        #if not es_area_reservada(fila, col):
        matriz[fila, col] = 1 - int(datos[datos_index])  # Insertar bit
        datos_index += 1
        # Mover al siguiente módulo
        if direction == -1:  # Zigzag hacia arriba
            if topeAbajo < 2:
                col -= 1
                cambio = 1
                topeAbajo += 1
            else:
                if fila > 0:
                    if cambio > 0:
                        fila -= 1
                        col += 1
                        cambio = 0
                    else:
                        cambio = 1
                        col -= 1 
                else:  # Llegó al borde superior, cambia de columna
                    if cambio > 0:
                        fila -= 1
                        col += 1
                        cambio = 0
                    else:
                        cambio = 1          
                        col -= 1
                    direction = 1
                    topeAbajo = 0
        else:  # Zigzag hacia abajo
            if topeArriba < 2:
                col -= 1
                cambio = 1
                topeArriba +=1
            else:
                if fila < 24:
                    if cambio > 0:
                        fila += 1
                        col += 1
                        cambio = 0
                    else:
                        cambio = 1
                        col -= 1
                else:  # Llegó al borde inferior, cambia de columna
                    if cambio > 0:
                        fila += 1
                        col += 1
                        cambio = 0
                    else:
                        cambio = 1
                        col -= 1
                    cambio = 0
                    direction = -1
                    topeArriba = 0
    
    #fila_final = fila
    #col_final = col
    #print(fila_final,col_final)
    return matriz

def save_qr(matriz, filename="qr_code.png"):
    
    #Convierte la matriz en una imagen y guarda el QR resultante.
    
    img = Image.fromarray((matriz * 255).astype('uint8'))  # Convertir 0/1 a 0/255 (negro/blanco)
    img = img.resize((250, 250), Image.NEAREST)  # Redimensionar para mejor visibilidad
    img.save(filename)

matriz = crear_qr_conmatriz()
mensaje_binario="0111011101110111011101110010111001100111011011110110111101100111011011000110010100101110011000110110111101101101"
matriz = insertar_mensaje(matriz, mensaje_binario)

save_qr(matriz)