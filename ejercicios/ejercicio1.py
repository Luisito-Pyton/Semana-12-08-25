class Estudiante:
    def __init__(self, nombre, semestre, carrera):
        self.nombre = nombre
        self.semestre = semestre
        self.carrera = carrera

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Semestre: {self.semestre}")
        print(f"Carrera: {self.carrera}")

estudiante1 = Estudiante("Edisson", 1, "Enfermeria")
estudiante1.mostrar_info()