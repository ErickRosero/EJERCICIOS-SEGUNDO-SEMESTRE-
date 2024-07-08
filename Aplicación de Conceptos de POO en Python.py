# Definición de la clase base Empleado
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        pass  # Este método será implementado en las clases derivadas


# Clase derivada EmpleadoRegular
class EmpleadoRegular(Empleado):
    def __init__(self, nombre, salario_base, horas_extra, tarifa_horas_extra):
        super().__init__(nombre, salario_base)
        self.horas_extra = horas_extra
        self.tarifa_horas_extra = tarifa_horas_extra

    def calcular_salario(self):
        salario_total = self.salario_base + (self.horas_extra * self.tarifa_horas_extra)
        return salario_total


# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono, tarifa_comisiones):
        super().__init__(nombre, salario_base)
        self.bono = bono
        self.tarifa_comisiones = tarifa_comisiones

    def calcular_salario(self):
        salario_total = self.salario_base + self.bono + self.tarifa_comisiones
        return salario_total


# Función principal para probar el programa
def main():
    # Crear instancias de las clases
    empleado1 = EmpleadoRegular("Juan Pérez", 25000, 10, 100)
    gerente1 = Gerente("Ana Gómez", 40000, 5000, 0.05 * 40000)

    # Calcular y mostrar salarios
    salario_empleado1 = empleado1.calcular_salario()
    salario_gerente1 = gerente1.calcular_salario()

    print(f"Salario de {empleado1.nombre}: ${salario_empleado1}")
    print(f"Salario de {gerente1.nombre}: ${salario_gerente1}")


if __name__ == "__main__":
    main()
