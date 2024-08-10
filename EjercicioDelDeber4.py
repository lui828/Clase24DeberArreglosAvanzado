# Crea un arreglo con palabras que incluyan algunas duplicadas. Luego,
# elimina las palabras duplicadas y muestra el resultado.

palabras = ["rosas", "flores", "petalos", "rosas", "arboles", "hojas", "petalos", "frutos", "hojas"]
palabras_sin_duplicados = []
for palabras in palabras:
 if palabras not in palabras_sin_duplicados:
  palabras_sin_duplicados.append(palabras)

print("Arreglo sin duplicados:", palabras_sin_duplicados)
