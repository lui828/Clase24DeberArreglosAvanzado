# Crea un arreglo con una lista de palabras. Luego, cuenta cuántas veces aparece una palabra
# específica en el arreglo y muestra el resultado.

palabras = ["martillo", "cinta", "alicate", "tornillo", "martillo", "sierra", "foco", "martillo", "perno", "cincel"]

palabra_a_contar = "martillo"
contador = 0
for palabra in palabras:
 if palabra == palabra_a_contar:
  contador += 1

print(f"La palabra {palabra_a_contar} aparece {contador} veces en el arreglo.")
