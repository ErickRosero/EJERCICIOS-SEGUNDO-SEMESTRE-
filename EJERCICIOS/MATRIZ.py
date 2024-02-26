def buscar_valor(matriz, valor):
  """
  Función para buscar un valor específico en una matriz bidimensional.

  Parámetros:
    matriz: La matriz bidimensional en la que se realiza la búsqueda.
    valor: El valor específico que se busca.

  Retorno:
    Una tupla con las coordenadas (fila, columna) del valor encontrado, o (-1, -1) si no se encuentra.
  """
  filas = len(matriz)
  columnas = len(matriz[0])
  for fila in range(filas):
    for columna in range(columnas):
      if matriz[fila][columna] == valor:
        return fila, columna
  return -1, -1

# Ejemplo de uso
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
valor_buscado = 5

fila, columna = buscar_valor(matriz, valor_buscado)

if fila == -1 and columna == -1:
  print(f"El valor {valor_buscado} no se encuentra en la matriz")
else:
  print(f"El valor {valor_buscado} se encuentra en la posición ({fila}, {columna})")
