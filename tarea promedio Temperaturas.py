# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión ciudades (3 ciudades)
# Segunda dimensión semanas (4 semanas)
# Tercera dimensión dias de la semana (7 dias)
#from opcode import i

matriz_temp = [
    [  #ciudad Quito
        [  #semana
            {"semana1": "Quito", "lunes": 30},# dias
            {"semana1": "Quito", "martes": 29},
            {"semana1": "Quito", "miercoles": 29},
            {"semana1": "Quito", "jueves": 29},
            {"semana1": "Quito", "viernes": 28},
            {"semana1": "Quito", "sabado": 30},
            {"semana1": "Quito", "domingo": 29},
        ],
        [
            {"semana2": "Quito", "lunes": 29},
            {"semana2": "Quito", "martes": 29},
            {"semana2": "Quito", "miercoles": 30},
            {"semana2": "Quito", "jueves": 31},
            {"semana2": "Quito", "viernes": 28},
            {"semana2": "Quito", "sabado": 29},
            {"semana2": "Quito", "domingo": 30},
        ],
        [
            {"semana3": "Quito", "lunes": 29},
            {"semana3": "Quito", "martes": 26},
            {"semana3": "Quito", "miercoles": 28},
            {"semana3": "Quito", "jueves": 30},
            {"semana3": "Quito", "viernes": 29},
            {"semana3": "Quito", "sabado": 31},
            {"semana3": "Quito", "domingo": 29},
        ],
        [
            {"semana4": "Quito", "lunes": 30},
            {"semana4": "Quito", "martes": 29},
            {"semana4": "Quito", "miercoles": 28},
            {"semana4": "Quito", "jueves": 29},
            {"semana4": "Quito", "viernes": 30},
            {"semana4": "Quito", "sabado": 29},
            {"semana4": "Quito", "domingo": 28},
        ]
    ],
    [  # ciudad Muisne
        [  #semana
            {"semana1": "muisne", "lunes": 26},
            {"semana1": "muisne", "martes": 29},
            {"semana1": "muisne", "miercoles": 26},
            {"semana1": "muisne", "jueves": 27},
            {"semana1": "muisne", "viernes": 25},
            {"semana1": "muisne", "sabado": 28},
            {"semana1": "muisne", "domingo": 29},
        ],
        [
            {"semana2": "muisne", "lunes": 29},
            {"semana2": "muisne", "martes": 31},
            {"semana2": "muisne", "miercoles": 28},
            {"semana2": "muisne", "jueves": 31},
            {"semana2": "muisne", "viernes": 28},
            {"semana2": "muisne", "sabado": 29},
            {"semana2": "muisne", "domingo": 30},
        ],
        [
            {"semana3": "muisne", "lunes": 26},
            {"semana3": "muisne", "martes": 29},
            {"semana3": "muisne", "miercoles": 26},
            {"semana3": "muisne", "jueves": 30},
            {"semana3": "muisne", "viernes": 25},
            {"semana3": "muisne", "sabado": 28},
            {"semana3": "muisne", "domingo": 29}
        ],
        [
            {"semana4": "muisne", "lunes": 28},
            {"semana4": "muisne", "martes": 29},
            {"semana4": "muisne", "miercoles": 28},
            {"semana4": "muisne", "jueves": 29},
            {"semana4": "muisne", "viernes": 27},
            {"semana4": "muisne", "sabado": 22},
            {"semana4": "muisne", "domingo": 25}
        ]
    ],
    [# ciudad Babahoyo
       [#semana
           {"semana1": "babahoyo", "lunes": 31},
           {"semana1": "babahoyo", "martes": 29},
           {"semana1": "babahoyo", "miercoles": 30},
           {"semana1": "babahoyo", "jueves": 29},
           {"semana1": "babahoyo", "viernes": 28},
           {"semana1": "babahoyo", "sabado": 31},
           {"semana1": "babahoyo", "domingo": 31}
       ],
       [
           {"semana2": "babahoyo", "lunes": 30},
           {"semana2": "babahoyo", "martes": 29},
           {"semana2": "babahoyo", "miercoles": 31},
           {"semana2": "babahoyo", "jueves": 31},
           {"semana2": "babahoyo", "viernes": 29},
           {"semana2": "babahoyo", "sabado": 31},
           {"semana2": "babahoyo", "domingo": 30}
       ],
       [
           {"semana3": "babahoyo", "lunes": 31},
           {"semana3": "babahoyo", "martes": 29},
           {"semana3": "babahoyo", "miercoles": 30},
           {"semana3": "babahoyo", "jueves": 29},
           {"semana3": "babahoyo", "viernes": 31},
           {"semana3": "babahoyo", "sabado": 31},
           {"semana3": "babahoyo", "domingo": 31}
       ],
       [
           {"semana4": "babahoyo", "lunes": 29},
           {"semana4": "babahoyo", "martes": 31},
           {"semana4": "babahoyo", "miercoles": 30},
           {"semana4": "babahoyo", "jueves": 29},
           {"semana4": "babahoyo", "viernes": 31},
           {"semana4": "babahoyo", "sabado": 30},
           {"semana4": "babahoyo", "domingo": 31}
       ]
    ]
]

# Iteramos sobre cada ciudad
for ciudad_index, ciudad in enumerate(matriz_temp):
    print(f"Promedios semanales para la ciudad {ciudad[0][0].get('semana1')}:")

    # Iteramos sobre cada semana en la ciudad
    for semana_index, semana in enumerate(ciudad):
        suma_temperaturas = 0

        # Iteramos sobre los días de la semana para sumar las temperaturas
        for dia in semana:
            # Obtenemos solo los valores de temperatura, ignorando el nombre del día
            temperatura = list(dia.values())[-1]  # El último valor es la temperatura
            suma_temperaturas += temperatura

        # Calculamos el promedio de la semana
        promedio_semana = suma_temperaturas / 7
        print(f"  Semana {semana_index + 1}: {promedio_semana:.2f}°C")

    print("\n")  # Separación entre las ciudades












