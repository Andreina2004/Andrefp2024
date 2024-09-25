#diccionario información personal
#información personal
diccionario= {"nombre": "Efraín", "edad": 25, "ciudad": "Guayaquil", "profesión": "guardia de seguridad"}
#acceder al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente
diccionario["ciudad"]="Babahoyo"
# Agregar una nueva clave-valor para la profesión (ya está incluida)
diccionario["profesión"]="Docente"
#verificar la existencia de la clave "teléfono" existe caso contrario agregarla
if "teléfono"  not in diccionario:
    diccionario["teléfono"]="0988679336"
    #eliminar la clave "edad"
    del diccionario["edad"]
    #imprimir el diccionario final
    print(diccionario)
