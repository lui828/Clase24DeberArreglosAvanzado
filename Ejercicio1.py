# Crear un arreglo con números
numeros = [23, 45, 12, 89, 33, 67]
# Inicializar una variable para almacenar el valor máximo
maximo = numeros[0]
# Recorrer el arreglo para encontrar el máximo
for numero in numeros:
 if numero > maximo:
  maximo = numero
# Mostrar el valor máximo
print("El valor máximo es:", maximo)