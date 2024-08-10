# Crear un arreglo con números, incluyendo duplicados
numeros = [5, 3, 8, 3, 5, 1, 8, 7]
# Crear un nuevo arreglo para almacenar los números sin duplicados
numeros_sin_duplicados = []
# Recorrer el arreglo y agregar los números no duplicados al nuevo arreglo
for numero in numeros:
 if numero not in numeros_sin_duplicados:
  numeros_sin_duplicados.append(numero)
# Mostrar el nuevo arreglo sin duplicados
print("Arreglo sin duplicados:", numeros_sin_duplicados)