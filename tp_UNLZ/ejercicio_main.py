# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:19:33 2023

@author: Luis
"""
'''
Se importa el módulo que son las listas de cargas y parámetros de cada orígen y destino,
estas listas provienen de los exceles base de datos de la carpeta Matrices, se procesan con python 
para obtenerlas, para simplificar el ejemplo, ya se colocaron en forma de listas, donde cada
componente, tiene el formato de diccionario.Y también el módulo Pandas.
'''
import ejercicio
import pandas as pd

'''
Se transforma la lista base de cada producto en DataFrame, para visualizar mejor su
formato, y luego de lo expota como excel a la carpeta "resultados"
'''
carga_camion_mineria = pd.DataFrame(ejercicio.lista_camion_mineria)
carga_camion_mineria.to_excel('Matrices/resultados/Carga_Mineria_Aderivar.xlsx')

carga_camion_granos = pd.DataFrame(ejercicio.lista_camion_granos)
carga_camion_granos.to_excel('Matrices/resultados/Carga_Granos_Aderivar.xlsx')

'''
Se leen de un excel los criterios de derivabilidad de la carga.
'''
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

lista_derivable_mineria = calcular_derivabilidad(ejercicio.lista_camion_mineria, criterio)
lista_derivable_granos = calcular_derivabilidad(ejercicio.lista_camion_granos, criterio)

df_mineria = pd.DataFrame(lista_derivable_mineria)
df_mineria.to_excel('Matrices/resultados/Derivabilidad_mineria.xlsx')

df_granos = pd.DataFrame(lista_derivable_granos)
df_granos.to_excel('Matrices/resultados/Derivabilidad_granos.xlsx')

df_mineria = df_mineria.drop(['ID origen', 'ID destino', 'Distancia'], axis=1)
df_granos = df_granos.drop(['ID origen', 'ID destino', 'Distancia'], axis=1)

df_total_derivado = df_granos + df_mineria


df_total_derivado = df_total_derivado.replace({"OLAVARRIAOLAVARRIA": 'OLAVARRIA', "CABACABA":'CABA',"LA CARLOTALA CARLOTA": 'LA CARLOTA'})