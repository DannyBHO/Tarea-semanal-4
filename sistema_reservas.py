# Sistema de Reservas de Hotel
# Ejemplo del mundo real 

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def liberar(self):
        self.disponible = True


class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar_reserva(self):
        if self.habitacion.reservar():
            print(f"Reserva confirmada para {self.cliente} "
                  f"en la habitación {self.habitacion.numero}")
        else:
            print("La habitación no está disponible")


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        print("Habitaciones disponibles:")
        for h in self.habitaciones:
            if h.disponible:
                print(f"Habitación {h.numero} - {h.tipo} - ${h.precio}")


# -------- Programa principal --------

hotel = Hotel("Hotel Amazonía")

habitacion1 = Habitacion(101, "Simple", 40)
habitacion2 = Habitacion(102, "Doble", 60)

hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

hotel.mostrar_habitaciones_disponibles()

reserva1 = Reserva("Juan Pérez", habitacion1)
reserva1.confirmar_reserva()

hotel.mostrar_habitaciones_disponibles()
