# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:35:19 2023

@author: Luis
"""

import pandas as pd
 
miDicionario = {'nombres': ['Somu', 'Kiku', 'Amol', 'Lini'],
    'física': [68, 74, 77, 78],
    'química': [84, 56, 73, 69],
    'álgebra': [78, 88, 82, 87]}

#creación del dataframe
df = pd.DataFrame(miDicionario)
print('DataFrame Original\n--------------')
print(df)

#eliminación de la columna 
df = df.drop(['álgebra', 'química'], axis=1)
print('\n\nDataFrame despues de eliminar las columnas\n--------------')
print(df)