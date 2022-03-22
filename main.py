class Asiento:
    
    def __init__(self, color, precio, registro):
        self.color    = color
        self.precio   = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        coloresValidos = ["rojo", "verde", "amarillo", "negro", "blanco"]

        if (coloresValidos.count(color) > 0):
            self.color = color

class Auto:
    
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo   = modelo
        self.precio   = precio
        self.asientos = asientos
        self.marca    = marca
        self.motor    = motor
        self.registro = registro
    
    def cantidadAsientos(self):

        if type(self.asientos) == list:
            asientosReales = [x for x in self.asientos if type(x) == Asiento]
            return len(asientosReales)
        else:
            return 0
    
    def verificarIntegridad(self):
        integro = True

        if (type(self.motor) == Motor):
            if (self.motor.registro != self.registro):
                integro = False

        if type(self.asientos) == list:
            asientosReales   = [x for x in self.asientos  if type(x) == Asiento]
            asientosIntegros = [x for x in asientosReales if x.registro == self.registro]
            if (asientosReales != asientosIntegros):
                integro = False

        if (integro):
            return "Auto original"
        else:
            return "Las piezas no son originales"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo            = tipo
        self.registro        = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        tiposValidos = ["electrico", "gasolina"]

        if (tiposValidos.count(tipo) > 0):
            self.tipo = tipo

if __name__ == "__main__":
    a1 = Auto("model 3", 33000, [Asiento("blanco", 5000, 32),None, None, Asiento("blanco", 5000, 32), None],
              "tesla", Motor(4, "electrico", 32), 32)

    print(a1.cantidadAsientos())