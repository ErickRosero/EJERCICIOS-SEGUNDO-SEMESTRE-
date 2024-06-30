# Este programa es un buen ejemplo de cómo usar funciones para realizar cálculos y tomar decisiones basadas en esos cálculos. Además, cumple con las especificaciones al usar adecuadamente diferentes tipos de datos (float para el IMC), identificadores descriptivos (snake_case), y proporciona una funcionalidad clara y útil para calcular e interpretar el IMC de una persona.

def calcular_imc(peso_kg, altura_m):
    """
    Función que calcula el índice de masa corporal (IMC).

    Args:
    - peso_kg (float): Peso de la persona en kilogramos.
    - altura_m (float): Altura de la persona en metros.

    Returns:
    - float: Valor del IMC calculado.
    """
    imc = peso_kg / (altura_m ** 2)
    return imc


def interpretar_imc(imc):
    """
    Función que interpreta el valor del IMC y devuelve un mensaje.

    Args:
    - imc (float): Índice de masa corporal calculado.

    Returns:
    - str: Mensaje interpretativo del IMC.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal (saludable)"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


# Ejemplo de uso del programa:
if __name__ == "__main__":
    peso = 70  # kg
    altura = 1.75  # metros

    # Calcular IMC
    resultado_imc = calcular_imc(peso, altura)

    # Interpretar IMC
    interpretacion = interpretar_imc(resultado_imc)

    # Mostrar resultados
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"IMC: {resultado_imc:.2f}")
    print(f"Interpretación: {interpretacion}")
