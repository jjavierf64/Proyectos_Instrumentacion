# -*- coding: utf-8 -*-
"""Informe03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N3fOedPAFVASEPoe-YjMrfImF9y-A63h

# Instrumentación II G02 - Informe 03
## Subgrupo 01
## Integrantes:

* Maria Fernanda Quesada | 2020036474
* Jose Javier Fernández | 2020425930


## Instrucciones
Realizar:
* Una gráfica de $R_T$ a partir del archivo.csv, usando Python. Incluya los títulos de los ejes de forma adecuada.

* Una gráfica de $T$ a partir del archivo.csv, usando Python. Incluya los títulos de los ejes de forma adecuada.
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Gráfica Resistencia

ds = pd.read_csv('https://raw.githubusercontent.com/jjavierf64/Proyectos_Instrumentacion/main/S07/datos_22_03_22_14_30.csv')

print(ds.tail())

ds = ds.set_index('ts')

plt.plot(ds.ro)
plt.title('Medida del valor de la resistencia del termoresistor.')
plt.ylabel('Resitencia (Ohms)')
plt.xlabel('Tiempo (s)')
plt.show()

# Gráfica de Temperatura

plt.plot(ds.tk)
plt.title('Medida de la temperatura definida por el termoresistor.')
plt.ylabel('Temperatura (K)')
plt.xlabel('Tiempo (s)')
plt.show()

# Ambos Datos
plt.plot(ds.ro)
plt.plot(ds.tk)
plt.title('Medida de la resistencia y temperatura para un termoresistor.')
plt.ylabel('Magnitud')
plt.xlabel('Tiempo (s)')
plt.legend(['Resistencia (Ohms)','Temperatura (K)'],loc='upper left')
plt.show()
#No queda bien por la escala