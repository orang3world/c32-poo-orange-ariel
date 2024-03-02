from enum import Enum
import os
import random


# limpiar terminal antes de empezar
os.system("clear")


class TipoDeInstrum(Enum):

    PSN = "Percusion"
    VTO = "Viento"
    CDA = "Cuerda"


class Instrumento:

    def __init__(self, id, precio, tipoDeInstrum) -> None:
        self.id = id
        self.precio = precio
        self.tipoDeInstrum = TipoDeInstrum(tipoDeInstrum).value


class Sucursal:
    listaDeInstrum = []

    def __init__(self, nombreDeSuc) -> None:
        self.nombreDeSuc = nombreDeSuc

    def crear_instrumento(self, instrumento):
        # Agregar sucursal[0] e instrumento[1]
        self.listaDeInstrum.append([self.nombreDeSuc, instrumento]) 


class Fabrica:
    # un set para evitar repeticion de sucursales
    listaDeSuc = set()

    def __init__(self,nombreFabrica):
        self.nombreFabrica = nombreFabrica

    
    def crear_sucursal(self, nombreDeSuc):
        self.listaDeSuc.add(nombreDeSuc)
        
        
    ''' def listar_sucursales(self):
        print(self.listaDeSuc)'''
        
        
    def listar_instrumentos(self):
        for s in self.listaDeSuc:
            titulo = f'Sucursal : {s} '
            print('-'*len(titulo))
            print(titulo)
            print('-'*len(titulo))
            for i in Sucursal(s).listaDeInstrum:
                if i[0]== s:
                    print(i[1].id,i[1].precio,i[1].tipoDeInstrum)
            
            
    def listarInstrumentosPorTipo(self, tipo):
        for s in self.listaDeSuc:
            titulo = f'Sucursal : {s} --- filtro: {tipo}'
            print('-'*len(titulo))
            print(titulo)
            print('-'*len(titulo))
            for i in Sucursal(s).listaDeInstrum:
                if i[0]== s and i[1].tipoDeInstrum == TipoDeInstrum(tipo).value:
                    print(i[1].id,i[1].precio,i[1].tipoDeInstrum)
            print()
    

    def borrar_instrumentos(self):
        # buscar y mostrar el item
        target = input('Ingrese el id a borrar: ')
        print(f'Buscando id = {target}...\n')
        suc = list(self.listaDeSuc)[0]
        for i in Sucursal(suc).listaDeInstrum:
            if i[1].id == target:
                print('Objetivo encontrado:')
                print(f'Sucursal: {i[0]}  id: {i[1].id}\tprecio: {i[1].precio}\ttipo: {i[1].tipoDeInstrum}')
                opcion = input(f'confirma el borrado del instrumento con id = {i[1].id} (y / n): ')
                if opcion == 'y':
                    del Sucursal(suc).listaDeInstrum[Sucursal(suc).listaDeInstrum.index(i)] 
                    print('El instrumento ha sido borrado')
                    self.listar_instrumentos()
                    return
                else:
                    print('Operacion cancelada')
                    return
                    
        print('El id proporcionado no fue encontrado, intente nuevamente')


    def porcInstrumentosPorTipo(self, sucursal):
        cantCuerda=cantViento=cantPercusion=cantTotal=0

        for i in Sucursal(sucursal).listaDeInstrum:
            if i[0] == sucursal and i[1].tipoDeInstrum == 'Viento':
                cantViento += 1
                cantTotal += 1
            elif i[0] == sucursal and i[1].tipoDeInstrum == 'Cuerda':     
                cantCuerda += 1
                cantTotal += 1
            elif i[0] == sucursal and i[1].tipoDeInstrum == 'Percusion':     
                cantPercusion += 1
                cantTotal += 1
        print()
        titulo = f'Sucursal:  {sucursal}'
        subtitulo = 'Porcentajes de Instrumentos por su tipo : '
        print('-'*len(subtitulo))
        print(' '*int((len(subtitulo)-len(titulo))/2)+titulo+' '*int((len(subtitulo)-len(titulo))/2))
        print(subtitulo)
        print('-'*len(subtitulo))

        print(f'%CUERDA = {round(cantCuerda/cantTotal*100)}')
        print(f'%VIENTO = {round(cantViento/cantTotal*100)}')
        print(f'%PERCUSION = {round(cantPercusion/cantTotal*100)}')
                




# Creacion de instancias
sucursales = ['Central','Sur','Norte','Este','Oeste']
precios = list(range(100,1000))
# Creacion de sucursales
for s in sucursales:
    Fabrica('Ariel').crear_sucursal(s)
    # Creacion de 10 instrumentos por sucursal
    for i in range(1,11):
        tipo = random.choice(['Cuerda','Viento','Percusion'])
        idNum = str(sucursales.index(s)*10+i)
        Sucursal(s).crear_instrumento(Instrumento(idNum,random.choice(precios),tipo))
        
          
'''
for s in Fabrica.listaDeSuc:
    print(f'\n{s}\n')

    for i in Sucursal(s).listaDeInstrum:
        print(i.id,i.precio,i.tipoDeInstrum)
'''
# EJECUCIONES

Fabrica('Ariel').listar_instrumentos()
Fabrica('Ariel').listarInstrumentosPorTipo('Cuerda')
Fabrica('Ariel').borrar_instrumentos()
for s in Fabrica.listaDeSuc:
    Fabrica('Ariel').porcInstrumentosPorTipo(s)

