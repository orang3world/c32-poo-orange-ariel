class Producto:
    def __init__(self,id, cantidad, precioUnitario ) -> None:
        self.id = id
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario
    def mostrarProducto(self):
        pass
class Musica(Producto):
    def __init__(self, id, cantidad, precioUnitario, tituloCancion, autor, year) -> None:
        self.tituloCancion = tituloCancion
        self.autor = autor
        self.year = year
        super().__init__(id, cantidad, precioUnitario)
    def mostrarProducto(self):
        return super().mostrarProducto()

class Literatura(Producto):
    def __init__(self, id, cantidad, precioUnitario, tituloLibro, autor, year) -> None:
        self.tituloLibro = tituloLibro
        self.autor = autor
        self.year = year
        super().__init__(id, cantidad, precioUnitario)
    def mostrarProducto(self):
        return super().mostrarProducto()
    
class Cinematografia(Producto):
    def __init__(self, id, cantidad, precioUnitario, nombrePelicula, autor, year) -> None:
        self.nombrePelicula = nombrePelicula
        self.autor = autor
        self.year = year
        super().__init__(id, cantidad, precioUnitario)
    def mostrarProducto(self):
        return super().mostrarProducto()

song01 = Musica(1,1,200,'Imagine','Lennon',1971)
song02 = Musica(1,1,300,'Another Brick in the Wall','Pink Floyd',1979)
song03 = Musica(1,1,350,'Every Breath You Take','The Police',1983)

book01 = Literatura(1,1,3000,'Don Quijote de la Mancha','Cervantes',1615)
book02 = Literatura(1,1,3500,'Moby Dick','Herman Melville',1851)
book03 = Literatura(1,1,4000,'Los tres mosqueteros','Alejandro Dumas',1844)

movie01 = Cinematografia(1,1,200,'Back to the future','Robert Zemeckis',1985)
movie02 = Cinematografia(1,1,300,'Back to the future II','Robert Zemeckis',1989)
movie03 = Cinematografia(1,1,350,'Back to the future III','Robert Zemeckis',1990)