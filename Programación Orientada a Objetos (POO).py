class Dia:
  def __init__(self, temperatura):
    self.temperatura = temperatura

  def mostrar_temperatura(self):
    print(f"Temperatura del día: {self.temperatura:.2f}")

class Semana:
  def __init__(self):
    self.dias = []

  def agregar_dia(self, temperatura):
    nuevo_dia = Dia(temperatura)
    self.dias.append(nuevo_dia)

  def calcular_promedio_semanal(self):
    promedio = sum(dia.temperatura for dia in self.dias) / len(self.dias)
    return promedio

  def mostrar_promedio_semanal(self):
    promedio_semanal = self.calcular_promedio_semanal()
    print(f"Promedio semanal de temperatura: {promedio_semanal:.2f}")

semana = Semana()

for i in range(7):
  temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
  semana.agregar_dia(temperatura)

semana.mostrar_promedio_semanal()
