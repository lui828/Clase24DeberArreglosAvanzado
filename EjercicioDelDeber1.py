# Crea un arreglo con 7 números de tu elección y escribe un código que encuentre y muestre el valor mínimo.
numeros = [700, 1101, 65, 2, 34, 21, 645, 40]
minimo = numeros[3]
for numero in numeros:
 if numero > minimo:
  minimmo = numero

print("El valor minimo es:", minimo)