# crear una matriz  bidimensional 3x3 con valores numéricos
matriz = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

#valor a buscar
valor_a_buscar= 16
#iniciañizar variables para rastrear la posicion del valor
fila_encontrada=-1
columna_encontrada=-1
#recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range (len(matriz[fila])):
        if matriz[fila][columna]==valor_a_buscar:
            fila_encontrada= fila
            columna_encontrada= columna
            break
            #salir del bucle exterior si se encuentra el valor
            #verificar si se encontro el valor y mostrar la posición
if fila_encontrada != -1:
    print (f"se encontro{valor_a_buscar}en la fila{fila_encontrada}y columna{columna_encontrada}")
else:
    print(f"{valor_a_buscar}no se encontro en la matriz")
