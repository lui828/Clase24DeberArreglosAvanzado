# Crear un arreglo con algunos números
numeros = [4, 2, 7, 4, 8, 4, 1, 4]
# Elegir el número que queremos contar
valor_a_contar = 4
# Inicializar una variable para contar las ocurrencias
contador = 0
# Recorrer el arreglo y contar las veces que aparece el valor
for numero in numeros:
 if numero == valor_a_contar:
  contador += 1
# Mostrar el número de veces que aparece el valor
print(f"El número {valor_a_contar} aparece {contador} veces en el arreglo.")