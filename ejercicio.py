# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:19:33 2023

@author: Luis
"""
#%%
import pandas as pd

#%%
cargas_mineria =pd.read_excel('Matrices/Matrices Grupo Mineria_tp.xlsx',
                              sheet_name='Total Toneladas Mineria 2014', usecols=(range(1,5)))

#%%
criterio = pd.read_excel('Matrices/Criterios de derivabilidad_tp.xlsx', sheet_name='MINERIA') 

#%%
lista_camion = [{'Origen': 'OLAVARRIA',
  'ID origen': 1,
  'Destino': 'OLAVARRIA',
  'ID destino': 1,
  'Carga': 39319,
  'Distancia': 0},
 {'Origen': 'CABA',
  'ID origen': 2,
  'Destino': 'OLAVARRIA',
  'ID destino': 1,
  'Carga': 0,
  'Distancia': 0},
 {'Origen': 'LA CARLOTA',
  'ID origen': 3,
  'Destino': 'OLAVARRIA',
  'ID destino': 1,
  'Carga': 16948,
  'Distancia': 0},
 {'Origen': 'VENADO TUERTO',
  'ID origen': 4,
  'Destino': 'OLAVARRIA',
  'ID destino': 1,
  'Carga': 275000,
  'Distancia': 0},
 {'Origen': 'OLAVARRIA',
  'ID origen': 1,
  'Destino': 'CABA',
  'ID destino': 2,
  'Carga': 133000,
  'Distancia': 500},
 {'Origen': 'CABA',
  'ID origen': 2,
  'Destino': 'CABA',
  'ID destino': 2,
  'Carga': 34000,
  'Distancia': 0},
 {'Origen': 'LA CARLOTA',
  'ID origen': 3,
  'Destino': 'CABA',
  'ID destino': 2,
  'Carga': 1325674,
  'Distancia': 750},
 {'Origen': 'VENADO TUERTO',
  'ID origen': 4,
  'Destino': 'CABA',
  'ID destino': 2,
  'Carga': 12000000,
  'Distancia': 200},
 {'Origen': 'OLAVARRIA',
  'ID origen': 1,
  'Destino': 'LA CARLOTA',
  'ID destino': 3,
  'Carga': 1300,
  'Distancia': 0},
 {'Origen': 'CABA',
  'ID origen': 2,
  'Destino': 'LA CARLOTA',
  'ID destino': 3,
  'Carga': 2200,
  'Distancia': 0},
 {'Origen': 'LA CARLOTA',
  'ID origen': 3,
  'Destino': 'LA CARLOTA',
  'ID destino': 3,
  'Carga': 4200000,
  'Distancia': 0},
 {'Origen': 'VENADO TUERTO',
  'ID origen': 4,
  'Destino': 'LA CARLOTA',
  'ID destino': 3,
  'Carga': 0,
  'Distancia': 0},
 {'Origen': 'OLAVARRIA',
  'ID origen': 1,
  'Destino': 'VENADO TUERTO',
  'ID destino': 4,
  'Carga': 50000,
  'Distancia': 0},
 {'Origen': 'CABA',
  'ID origen': 2,
  'Destino': 'VENADO TUERTO',
  'ID destino': 4,
  'Carga': 15000,
  'Distancia': 0},
 {'Origen': 'LA CARLOTA',
  'ID origen': 3,
  'Destino': 'VENADO TUERTO',
  'ID destino': 4,
  'Carga': 65000,
  'Distancia': 0},
 {'Origen': 'VENADO TUERTO',
  'ID origen': 4,
  'Destino': 'VENADO TUERTO',
  'ID destino': 4,
  'Carga': 10000,
  'Distancia': 0}]

#%%
def calcular_derivabilidad(lista_cargas, derivabilidad):
    """ Lee una lista de bibliotecas con informacion de cargas, origen, destino y distancia
    y utiliza criterios de derivavilidad al FFCC para crear una lista nueva similar pero
    con las cargas derivables.
    """
    derivable = []
    for i in lista_cargas:
        conjunto = {}
        conjunto['Origen'] = i['Origen']
        conjunto['ID origen'] = i['ID origen']
        conjunto['Distancia'] = i['Distancia']
        conjunto['ID destino'] = i['ID destino']
        conjunto['Destino'] = i['Destino']
        if 300 > i['Distancia'] >= 200:
            if criterio.iat[2,0] > i['Carga'] >= criterio.iat[3,0] :
                conjunto['Carga'] = i['Carga']*criterio.iat[3,4]
            elif criterio.iat[1,0] > i['Carga'] >= criterio.iat[2,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[2,4]
            elif criterio.iat[0,0] > i['Carga'] >= criterio.iat[1,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[1,4]
            elif i['Carga'] >= criterio.iat[0,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[0,4]
            else:
                conjunto['Carga'] = 0
        elif 400 > i['Distancia'] >= 300:
            if criterio.iat[2,0] > i['Carga'] >= criterio.iat[3,0] :
                conjunto['Carga'] = i['Carga']*criterio.iat[3,3]
            elif criterio.iat[1,0] > i['Carga'] >= criterio.iat[2,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[2,3]
            elif criterio.iat[0,0] > i['Carga'] >= criterio.iat[1,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[1,3]
            elif i['Carga'] >= criterio.iat[0,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[0,3]
            else:
                conjunto['Carga'] = 0
        elif 500 > i['Distancia'] >= 400:
            if criterio.iat[2,0] > i['Carga'] >= criterio.iat[3,0] :
                conjunto['Carga'] = i['Carga']*criterio.iat[3,2]
            elif criterio.iat[1,0] > i['Carga'] >= criterio.iat[2,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[2,2]
            elif criterio.iat[0,0] > i['Carga'] >= criterio.iat[1,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[1,2]
            elif i['Carga'] >= criterio.iat[0,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[0,2]
            else:
                conjunto['Carga'] = 0
        elif i['Distancia'] >= 500:
            if criterio.iat[2,0] > i['Carga'] >= criterio.iat[3,0] :
                conjunto['Carga'] = i['Carga']*criterio.iat[3,1]
            elif criterio.iat[1,0] > i['Carga'] >= criterio.iat[2,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[2,1]
            elif criterio.iat[0,0] > i['Carga'] >= criterio.iat[1,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[1,1]
            elif i['Carga'] >= criterio.iat[0,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[0,1]
            else:
                conjunto['Carga'] = 0
        else:
            conjunto['Carga'] = 0
        derivable.append(conjunto)
        
    return derivable 
#%%