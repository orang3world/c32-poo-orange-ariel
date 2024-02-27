from ast import arg
from http import client
import os

from click import argument

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
    def __init__(self, dni, nombre, apellido, añoIngreso, relContractual) -> None:
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.añoIngreso = añoIngreso
        self.relContractual = relContractual
        
    def calcularSalario(self):
        pass
    def mostrarSalario(self):
        pass
    
class PorComision(Empleado):
    def __init__(self, dni, nombre, apellido, añoIngreso, relContractual, salarioMinimo, clientesCaptados, montoPorCliente ) -> None:
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente
        
        super().__init__(dni, nombre, apellido, añoIngreso, relContractual)
        
    def calcularSalario(self, salarioMinimo, clientesCaptados, montoPorCliente):
        comision = clientesCaptados * montoPorCliente
        if comision > salarioMinimo:
            salario = salarioMinimo + comision
            return salario
        else:
            return salarioMinimo
    def empleadoConMasClientes(self):
        pass
        
        
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
            
    
    

empl01 = Empleado('12345678','Ariel', 'Sanchez',1985, 'PorComision')
empl02 = Empleado('87654321','Juan', 'Fernandez',2005, 'PorComision')
empl03 = Empleado('22233344','Cecilia', 'Garcia',2022, 'PorComision')
empl04 = Empleado('33344455','Alicia', 'Mendoza',2009, 'SalarioFijo')
empl05 = Empleado('44455566','Fennando' , 'Olavarria',2020, 'SalarioFijo')
empl06 = Empleado('66677788','German', 'Larrea',2000, 'SalarioFijo')

for empleado in Empleado(*):
    print(empleado.dni)