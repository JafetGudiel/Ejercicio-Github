# Solicitar al usuario el nombre del estudiante y sus notas
nombre_estudiante = (input(f"Ingrese el nombre del estudisnte:  "))
notas = []
for i in range(4):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

# Calcular el promedio
promedio = sum(notas)/len(notas)

# Guardar los datos en el archivo "notas.txt"
with open('promedios.txt', "a") as archivo:
    archivo.write(f"Nombre del estudiante: {nombre_estudiante}\n")
    archivo.write("Notas: " + ", ".join(map(str, notas)) + "\n")
    archivo.write(f"Promedio: {promedio}\n\n")

print("Datos guardados en el archivo 'notas.txt'.")
