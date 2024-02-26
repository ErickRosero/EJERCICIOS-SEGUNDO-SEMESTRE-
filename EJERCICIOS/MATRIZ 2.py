def ordenar_fila(matriz, fila):
  """
  Función para ordenar una fila específica de una matriz bidimensional en orden ascendente.

  Parámetros:
    matriz: La matriz bidimensional en la que se ordena la fila.
    fila: El índice de la fila que se desea ordenar.

  Retorno:
    La matriz original con la fila ordenada.
  """
  # Se ordena la fila usando el método de ordenamiento por burbuja
  for i in range(len(matriz[fila]) - 1):
    for j in range(len(matriz[fila]) - i - 1):
      if matriz[fila][j] > matriz[fila][j + 1]:
        matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]
  return matriz

# Ejemplo de uso
matriz = [[1, 5, 3], [4, 2, 6], [7, 8, 9]]
fila_a_ordenar = 0

matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

print(f"Matriz original:")
for fila in matriz:
  print(fila)

print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
for fila in matriz_ordenada:
  print(fila)
