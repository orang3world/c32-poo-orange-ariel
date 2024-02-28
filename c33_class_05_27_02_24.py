
"""
Los objetos son instancias de las clases

diagrama uml (juntos)
codigo (solos)

"""

import datetime
from datetime import datetime
from enum import Enum
import os

os.system('clear' or 'cls')



class TipoContrato(Enum):
    FIJO = "Salario Fijo"
    COMI = "Por Comision"
    
class Antiguedad(Enum):
    CAT1 = "Menos de 2 años"
    CAT2 = "De 2 a 5 años"
    CAT3 = "Mas de 5 años"


class Empleado:
    # instancias ordenadas en listas
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
        else:
            self.__class__.emplSalarioFijo.append(self)

        
    def calcularSalario(self):
        pass
    
    
    def mostrarSalario():
        
        # titulo
        print('----------------------------------')
        print('Listado de empleados por comision:')
        print('----------------------------------')
        
        # ancho de columan para la presentacion en terminal
        anchoColumna = 15
        # iteracion por las instancias PorComision
        for empl in Empleado.emplPorComision:
            # Calcular el salario de cada instancia
            salarioPorComision = empl.calcularSalario(empl.salarioMinimo,empl.clientesCaptados,empl.montoPorCliente)
            # llenar con espacios cada str para un ancho de columna comun
            espacios = anchoColumna-len(str(salarioPorComision))
            print(empl.nombre+' '*(anchoColumna-len(empl.nombre)), 
                   empl.apellido+' '*(anchoColumna-len(empl.apellido)),
                   ' '*(espacios)+str(salarioPorComision))
            
        # titulo
        print('--------------------------------------')
        print('Listado de empleados con salario fijo:')
        print('--------------------------------------')
        
        # ordenar las instancias por salario
        Empleado.emplSalarioFijo = sorted(Empleado.emplSalarioFijo, key=lambda empl:empl.calcularSalario(empl.sueldoBasico,empl.añoIngreso), reverse=True)
        # iteracion por las instancias SalarioFijo
        for empl in Empleado.emplSalarioFijo:
            # Calcular el salario de cada instancia
            salarioFijoValor = empl.calcularSalario(empl.sueldoBasico,empl.añoIngreso)
            # llenar con espacios casa str para un ancho de columna comun
            espacios = anchoColumna-len(str(salarioPorComision))
            print(empl.nombre+' '*(15-len(empl.nombre)), 
                   empl.apellido+' '*(15-len(empl.apellido)),
                   ' '*(espacios)+str(salarioFijoValor))
        print()    
                

    
class PorComision(Empleado):
    
    
    def __init__(self, dni, nombre, apellido, añoIngreso, relContractual, salarioMinimo, clientesCaptados, montoPorCliente ) -> None:
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente
        super().__init__(dni, nombre, apellido, añoIngreso, relContractual)
        
        
    def calcularSalario(self, salarioMinimo, clientesCaptados, montoPorCliente):
        
        comision = clientesCaptados * montoPorCliente
        # si la comision es menor al salario minimo, recibe el salario minimo, sino la comision.
        if comision > salarioMinimo:
            salario = comision
            return float(salario)
        else:
            salario = salarioMinimo
            
        return float(salario)
    
    
    def empleadoConMasClientes():
        # ordenar las instancias 'PorComision' por clientesCaptados, orden descendente.
        Empleado.emplPorComision = sorted(Empleado.emplPorComision, key=lambda employee:employee.clientesCaptados, reverse=True)
        # tomar el primero de la lista (el mayor valor)
        empl = Empleado.emplPorComision[0]
        texto = f'El empleado con mas clientes captados es : {empl.nombre} {empl.apellido}. cantidad: {empl.clientesCaptados} clientes.'
        print('\n'+'-'*len(texto))
        print(texto)
        print('-'*len(texto))
        
        
    def rankingMasClientes():
        # ordenar las instancias 'PorComision' por clientesCaptados, orden descendente.
        Empleado.emplPorComision = sorted(Empleado.emplPorComision, key=lambda employee:employee.clientesCaptados, reverse=True)
        # tomar el primero de la lista (el mayor valor)
        empl = Empleado.emplPorComision[0:3]
        texto = 'El ranking de los empleados con mas clientes captados es : '
        print('\n'+'-'*len(texto))
        print(texto)
        print('-'*len(texto))
        print()
        for e in empl:
            print(f'{empl.index(e)+1}° lugar: ',e.nombre,e.apellido,e.clientesCaptados)
         
        
        
class SalarioFijo(Empleado):
    
    porcAdicional = {'CAT1':1,'CAT2':1.05,'CAT3':1.1}
    
    def __init__(self, dni, nombre, apellido, añoIngreso, relContractual, sueldoBasico) -> None:
        self.sueldoBasico = sueldoBasico
        super().__init__(dni, nombre, apellido, añoIngreso, relContractual)
        
        
    def calcularSalario(self, sueldoBasico, añoIngreso):
        year = datetime.now().year   
        antiguedad = year - añoIngreso     
        
        if antiguedad < 2:
            salario = sueldoBasico * SalarioFijo.porcAdicional['CAT1']
        elif antiguedad < 5:
            salario = sueldoBasico * SalarioFijo.porcAdicional['CAT2']
        else:
            salario = sueldoBasico * SalarioFijo.porcAdicional['CAT3']
            
        return float(salario)
            
    
    

empl01 = PorComision('12345678','Ariel', 'Sanchez',1985, 'porComision',1000000, 50, 15000)
empl02 = PorComision('11223344','Alejandro', 'Gomez',1995, 'porComision',1000000, 100, 15000)
empl03 = PorComision('11122233','Brian', 'Figueroa',2005, 'porComision',1000000, 200, 15000)
empl04 = PorComision('11112222','Carlos', 'Colombo',2015, 'porComision',1000000, 300, 15000)
empl05 = PorComision('33334444','Cecilia', 'Garcia',2022, 'porComision',1000000, 500, 15000)
empl06 = SalarioFijo('55556666','Alicia', 'Mendoza',2009, 'salarioFijo',2000000)
empl07 = SalarioFijo('77778888','Maria' , 'Lorenzo',2010, 'salarioFijo',2000000)
empl08 = SalarioFijo('99990000','Laura', 'Salguero',2023, 'salarioFijo',3000000)
empl09 = SalarioFijo('22222222','Macarena', 'Silverado',2021, 'salarioFijo',3000000)
empl10 = SalarioFijo('33333333','German', 'Larrea',2018, 'salarioFijo',4000000)


PorComision.empleadoConMasClientes()
PorComision.rankingMasClientes()
print()
Empleado.mostrarSalario()
