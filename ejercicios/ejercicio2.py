class Habitacion:
    def __init__(self, tipo, precio_noche):
        self.tipo = tipo
        self.precio_noche = precio_noche

    def calcular_total(self, noches):
        return self.precio_noche * noches

class Hotel:
    def __init__(self):
        self.habitaciones = {
            'simple': Habitacion('simple', 50),
            'doble': Habitacion('doble', 80),
            'suite': Habitacion('suite', 120)
        }

    def calcular_precio(self, tipo_habitacion, noches):
        if tipo_habitacion not in self.habitaciones:
            return "Tipo de habitación no válido"
        habitacion = self.habitaciones[tipo_habitacion]
        return habitacion.calcular_total(noches)

hotel = Hotel()
print(hotel.calcular_precio("suite", 2))
