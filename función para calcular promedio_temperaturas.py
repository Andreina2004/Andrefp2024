#Función que calcule el  promedio de temperaturas de múltiples ciudades y semanas.
#datos_temperaturas
def temperatura_promedio(ciudades_temperaturas):
    """
    Esta función calcula la temperatura promedio de un conjunto de ciudades.
    Args:
        ciudades_temperaturas (dict): Un diccionario que contiene nombres de ciudades como claves
                                      y listas de temperaturas como valores.
    Returns:
        dict: Un diccionario que contiene nombres de ciudades como claves
              y temperaturas promedio como valores.
              :param ciudades_temperaturas:
              :return:
    """
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Creamos un diccionario de ciudades y temperaturas
ciudades_temperaturas = {
           "Quito":[30,29,30,31,29,29,28],
          "Muisne":[29,29,28,27,29,30,29],
          "Babahoyo":[30,30,31,31,29,30,30]
}
#Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")











