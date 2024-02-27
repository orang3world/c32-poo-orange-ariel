
"""
Los objetos son instancias de las clases

diagrama uml (juntos)
codigo (solos)

"""
import datetime
from datetime import datetime
 

from enum import Enum


class TipoContrato(Enum):
    FIJO = "Salario Fijo"
    COMI = "Por Comision"
    
class Antiguedad(Enum):
    CAT1 = "Menos de 2 años"
    CAT2 = "De 2 a 5 años"
    CAT3 = "Mas de 5 años"


class Empleado:
    
    empleados = []
    emplPorComision = []
    emplSalarioFijo = []

    def __init__(self, dni, nombre, apellido, añoIngreso, relContractual) -> None:
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.añoIngreso = añoIngreso
        self.relContractual = relContractual
        if relContractual == 'porComision':
            self.__class__.emplPorComision.append(self)
        elif relContractual == 'salarioFijo':
            self.__class__.emplSalarioFijo.append(self)
        else:
            self.__class__.empleados.append(self)



        self.__class__.empleados.append(self)
        
    def calcularSalario(self):
        pass
    def mostrarSalario():
        print('Listado de empleados por comision:')
        for empl in Empleado.emplPorComision:
             print(f'\tNombre : {empl.nombre} {empl.apellido}. Salario:  {empl.calcularSalario(empl.salarioMinimo,empl.clientesCaptados,empl.montoPorCliente)} ')
        print('Listado de empleados con salario fijo :')
        for empl in Empleado.emplSalarioFijo:
             print(f'\t Persona : {empl.nombre} {empl.apellido}. Salario:  {empl.calcularSalario(empl.sueldoBasico,empl.añoIngreso)} ')


    
class PorComision(Empleado):
    
    
    def __init__(self, dni, nombre, apellido, añoIngreso, relContractual, salarioMinimo, clientesCaptados, montoPorCliente ) -> None:
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente
        super().__init__(dni, nombre, apellido, añoIngreso, relContractual)
        
    def calcularSalario(self, salarioMinimo, clientesCaptados, montoPorCliente):
        comision = clientesCaptados * montoPorCliente
        if comision > salarioMinimo:
            salario = comision
            return salario
        else:
            salario = salarioMinimo
        return salario
    
    
    def empleadoConMasClientes():
        
        Empleado.emplPorComision = sorted(Empleado.emplPorComision, key=lambda employee:employee.clientesCaptados, reverse=True)
        empl = Empleado.emplPorComision[0]
        print(f'El empleado con mas clientes captados es : {empl.nombre} {empl.apellido}. Con {empl.clientesCaptados} clientes captados.')
         
        
        
class SalarioFijo(Empleado):
    def __init__(self, dni, nombre, apellido, añoIngreso, relContractual, sueldoBasico, porcAdicional) -> None:
        self.sueldoBasico = sueldoBasico
        self.porcAdicional = porcAdicional
        
        super().__init__(dni, nombre, apellido, añoIngreso, relContractual)
        
    def calcularSalario(self, sueldoBasico, añoIngreso, ):
        year = datetime.now().year   
        antiguedad = year - añoIngreso     
        
        if antiguedad < 2:
            salario = sueldoBasico
        elif antiguedad < 5:
            salario = sueldoBasico * 1.05
        else:
            salario = sueldoBasico * 1.1
        return salario
            
    
    

empl01 = PorComision('12345678','Ariel', 'Sanchez',1985, 'porComision',1000000, 500, 15000)
empl02 = PorComision('11223344','Alejandro', 'Gomez',1995, 'porComision',1000000, 1300, 15000)
empl03 = PorComision('11122233','Brian', 'Figueroa',2005, 'porComision',1000000, 200, 15000)
empl04 = PorComision('11112222','Carlos', 'Colombo',2015, 'porComision',1000000, 100, 15000)
empl05 = PorComision('33334444','Cecilia', 'Garcia',2022, 'porComision',1000000, 50, 15000)
empl06 = SalarioFijo('55556666','Alicia', 'Mendoza',2009, 'salarioFijo',2000000, 23)
empl07 = SalarioFijo('77778888','Maria' , 'Lorenzo',2010, 'salarioFijo',2000000, 23)
empl08 = SalarioFijo('99990000','Laura', 'Salguero',2023, 'salarioFijo',3000000, 23)
empl09 = SalarioFijo('22222222','Macarena', 'Silverado',2021, 'salarioFijo',3000000, 23)
empl10 = SalarioFijo('33333333','German', 'Larrea',2018, 'salarioFijo',4000000, 23)


PorComision.empleadoConMasClientes()
print()
Empleado.mostrarSalario()
