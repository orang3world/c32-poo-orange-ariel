"""
Clase 04 del curso de programacion en Python con orientacion a objetos
"""

class Auto:
    def __init__(self, marca, modelo, color,tipoCombustible, cantPuertas) -> None:
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipoCombustible = tipoCombustible
        self.cantPuertas = cantPuertas
    
    # realizar alguna accion tocar bocina
        
    # setters y getters
        # set - setear - establecer un valor
        # getter -nos devuelve un valor

    def getMarca(self):
        return self.marca
    def getColor(self):
        return self.color
    def getModelo(self):
        return self.modelo
    def getTipoCombustible(self):
        return self.tipoCombustible
    def getCantPuertas(self):
        return self.cantPuertas
    def getEstado(self):
        return self.estado
        
    def mostrarAuto(self):
        print("Marca: {}",
            "Modelo: {}",
            "Color: {self.getColor()}",\
            "Combustible: {self.getTipoCombustible()}",\
            "Puertas: {self.getCantPuertas()}",format(self.getMarca(),self.getModelo()))

marca = input("ingresar marca")         
modelo = input("ingresar modelo")         
color = input("ingresar color") 
tipoCombustible = input("ingresar tipo de Combustible")      

auto1 = Auto("Toyota","Prius","Rojo","Hibrido","4")
auto2 = Auto("Ford","fiesta","azul","Diesel","3")
auto3 = Auto("Ford","fiesta","azul","Diesel","3")

auto1.mostrarAuto()
auto2.mostrarAuto()
auto3.mostrarAuto()