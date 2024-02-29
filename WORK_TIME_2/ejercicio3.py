""" 
3. A partir del siguiente enunciado, crear las clases necesarias (con
sus respectivos atributos y métodos) para poder representarlos.

↪ “Juan Lopez tiene 25 años y es de profesión Abogado. Por la tarde, después de 
 trabajar, sale a caminar. También 
 tiene una bicicleta amarilla  marca “Massino” y a veces sale a dar
vueltas en ella”.

name: Juan
lastName: Lopez
age: 25
proffesion: Layer
activity: worker
hobby: to walk
sport:bike riding
transport: bicicle
bicicle band: Massino
"""



from turtle import color

from more_itertools import one


class Pearson:
    def __init__(self, firsName, lastName, age) -> None:
        self.firsName = firsName
        self.lastNanme = lastName
        self.age = age
    def iAm(self):
        print(f"My name is : {self.firsName}")
        print(f"my last name is : {self.lastNanme}")
        print(f"I'm {self.age} years old")

class Profession(Pearson):
    def __init__(self, firsName, lastName, age, profession) -> None:
        self.profession = profession
        super().__init__(firsName, lastName, age)

    def myProfessionIs(self):
        print(f"I'm {self.profession}")
class hobby(Pearson):
    def __init__(self, firsName, lastName, age, hobby1, hobby2) -> None:
        self.hobby1 = hobby1
        self.hobby2 = hobby2
        super().__init__(firsName, lastName, age)
    def myHobbies(self):
        print(f"my hobbies are: {self.hobby1} and {self.hobby2}")
class mobility(Pearson):
    def __init__(self, firsName, lastName, age, mobility, color, brand) -> None:
        self.mobility = mobility
        self.color = color
        self.brand = brand
        super().__init__(firsName, lastName, age)
    def myMobility(self):
        print(f"Mobility By {self.mobility} color {self.color} and {self.brand} brand ")

onePearson = Pearson("Juan","Lopez","25")
onePearson.iAm()

oneProfession = Profession(onePearson.firsName,onePearson.lastNanme,onePearson.age,"Layer")
oneProfession.myProfessionIs()

oneHobby = hobby(onePearson.firsName,onePearson.lastNanme,onePearson.age,"to walk", "bike riding")
oneHobby.myHobbies()
oneMobility = mobility(onePearson.firsName,onePearson.lastNanme,onePearson.age,"bicicle","yellow", "Massino")
oneMobility.myMobility()