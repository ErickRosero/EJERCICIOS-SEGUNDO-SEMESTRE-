# Ejemplo de un sistema de gestión de reservas utilizando POO

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Reserva:
    def __init__(self, cliente, fecha, num_personas):
        self.cliente = cliente
        self.fecha = fecha
        self.num_personas = num_personas
        self.confirmada = False

    def confirmar_reserva(self):
        self.confirmada = True

    def mostrar_reserva(self):
        print(f"Reserva para {self.cliente.nombre} el {self.fecha} para {self.num_personas} personas")

# Crear instancias de Cliente y Reserva
cliente1 = Cliente("Erick", "erick2610@email.com")
reserva1 = Reserva(cliente1, "2024-06-29", 10)

# Interacción entre objetos
reserva1.mostrar_reserva()
reserva1.confirmar_reserva()
print(f"La reserva está confirmada: {reserva1.confirmada}")