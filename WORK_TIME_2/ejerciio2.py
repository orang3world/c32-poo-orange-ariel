"""
2. Crear una clase llamada Animal, otra llamada Perro y otra llamada
Águila.
↪ La clase Animal tiene:
○ atributo cantidad_patas: numérico
○ atributo tipo: vertebrado/invertebrado
○ método comer(): retorna un string “estoy comiendo”

↪ La clase Perro hereda de Animal y agrega:
○ atributo nombre: texto
○ atributo raza: texto
○ método correr(): retorna un string “estoy corriendo”

↪ La clase Aguila hereda de Animal y agrega:
○ método volar(): retorna un string “estoy volando”
"""

class Animal:
    def __init__(self, patas, tipo) -> None:
        self.patas = int(patas)
        self.tipo = str(tipo)
    def comer(self):
        print("estoy comiendo")

class Perro(Animal):
    def __init__(self, patas, tipo, nombre, raza) -> None:
        self.nombre = nombre
        self.raza = raza
        super().__init__(patas, tipo)

    def correr(self):
        print("estoy corriendo")

class Aguila(Animal):
    def __init__(self, patas, tipo) -> None:
        super().__init__(patas, tipo)
    def volar(self):
        print("estoy volando")

imperial = Aguila("2", "Vertebrado")
myDog = Perro("4", "Vertebrado", "Max", "Labrador")

imperial.volar()
print(f"I'm a dog: \n my name is: {myDog.nombre} \n I have {myDog.patas} legs \n"); myDog.correr()