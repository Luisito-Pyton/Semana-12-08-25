class Factura:
    def __init__(self, precio, tasa_iva=0.19):
        self.precio = precio
        self.tasa_iva = tasa_iva

    def calcular_iva(self):
        return self.precio * self.tasa_iva

    def calcular_total(self):
        return self.precio + self.calcular_iva()

    def mostrar_detalle(self):
        print(round(self.calcular_iva(), 2))
        print(round(self.calcular_total(), 2))


precio_producto = float(input())
factura = Factura(precio_producto)
factura.mostrar_detalle()