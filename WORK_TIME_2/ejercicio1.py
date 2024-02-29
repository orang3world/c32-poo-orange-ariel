""" 

Desafío🎯:

1. Crear una clase llamada Bicicleta y luego aplica los siguientes
accionables:
↪ Agregar al menos 3 atributos
↪ Agregar al menos 3 métodos
↪ Agregar el método constructor de la clase.

"""

class Bicicleta:
    # init method or constructor
    def __init__(self, uso, rodado, color):
        # Instance Variable
        self.uso = uso
        self.rodado = rodado 
        self.color = color
        # Sample Method
    def bikeFor(self):
        print('bicileta para:', self.uso)
    def bikeRodado(self):
        print('bicileta rodado:', self.rodado)
    def bikeColor(self):
        print('bicileta color:', self.color)

myBike = Bicicleta( "MountainBike", "26", "Green")

myBike.bikeFor()
myBike.bikeRodado()
myBike.bikeColor()