def calcular_descuento(monto_compra):
  """
  Calcula el descuento en una compra en función del monto total.

  Args:
      monto_compra (float): El monto total de la compra.

  Returns:
      float: El monto final a pagar.
  """

  if monto_compra < 100:
    descuento = 0
  elif monto_compra < 250:
    descuento = monto_compra * 0.10
  else:
    descuento = monto_compra * 0.15

  monto_final = monto_compra - descuento
  return monto_final


# Ejemplo de uso
monto_compra = float(input("Ingrese el monto total de la compra: "))
monto_final = calcular_descuento(monto_compra)

print(f"El monto final a pagar es: ${monto_final:.2f}")
