#crear un programa que calcule el descuento en compras en función del monto total de la compra y mostrar el monto final a pagar.
# definir la función con parametros
# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=15):
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamada a la función con solo el monto total
monto1 = 150  # Ejemplo de monto total
descuento1, monto_final1 = calcular_descuento(monto1)

# Llamada a la función con monto total y porcentaje de descuento específico
monto2 = 300  # segundo ejemplo de monto total
porcentaje_descuento2 = 20  # Porcentaje de descuento específico
descuento2, monto_final2 = calcular_descuento(monto2, porcentaje_descuento2)

# Mostrar resultados
print(f"Monto total: ${monto1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar: ${monto_final1}")
print()  # Espacio en blanco para separar los resultados
print(f"Monto total: ${monto2}")
print(f"Descuento aplicado: ${descuento2}")
print(f"Monto final a pagar: ${monto_final2}")
