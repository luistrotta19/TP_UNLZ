# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:19:33 2023

@author: Luis
"""

import ejercicio

import pandas as pd

carga_camion_mineria = pd.DataFrame(ejercicio.lista_camion)
carga_camion_mineria.to_excel('Matrices/Carga_Mineria_Aderivar.xlsx')

cargas_mineria = pd.read_excel('Matrices/Matrices Grupo Mineria_tp.xlsx',sheet_name='Total Toneladas Mineria 2014', usecols=(range(1,5)))

criterio = pd.read_excel('Matrices/Criterios de derivabilidad_tp.xlsx', sheet_name='MINERIA') 




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
            elif criterio.iat[0,0] > i['Cargcls'] >= criterio.iat[1,0]:
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

lista_derivable = calcular_derivabilidad(ejercicio.lista_camion, criterio)

df = pd.DataFrame(lista_derivable)
df.to_excel('Matrices/Derivabilidad_mineria_3.xlsx')