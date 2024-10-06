#escritura en el archivo de texto
# Abre el archivo my_notes.txt en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribir tres líneas de notas personales en el archivo
    file.write("Primer nota: El amor y la esperanza nunca debe faltar.\n")
    file.write("Segunda nota: Los archivos de texto son utiles y sirven para guardar imformación importante.\n")
    file.write("Tercera nota: Tu puedes ser todo lo que quieras ser porque los límites los pones tú!.\n")
# El archivo se cierra automáticamente al salir del bloque 'with'
# Lectura del archivo de texto
# Abre el archivo my_notes.txt en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Lee el contenido del archivo línea por línea
    for line in file:
        # Muestra cada línea leída en la consola
        print(line.strip())  # strip() elimina espacios o saltos de línea adicionales
# El archivo se cierra automáticamente al salir del bloque 'with'
