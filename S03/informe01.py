# -*- coding: utf-8 -*-
"""Informe01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AyPrZpOepGhdubusNHkWHTdCfT7nNm9a

# Instrumentación II G02 - Tarea 1
## Subgrupo 01
## Integrantes:

* Maria Fernanda Quesada | 2020036474
* Jose Javier Fernández | 2020425930


## Instrucciones
Realizar:
* Una gráfica de *i* a partir del archivo.csv, usando Python. Incluya los títulos de los ejes de forma adecuada.

* Una gráfica de *v* a partir del archivo.csv, usando Python. Incluya los títulos de los ejes de forma adecuada.
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Gráfica de Corriente i

ds = pd.read_csv('https://raw.githubusercontent.com/jjavierf64/Proyectos_Instrumentacion/main/S03/datosCor01.csv')

print(ds.tail())

ds = ds.set_index('t')

plt.plot(ds.c)
plt.title('Medida de la corriente en un potenciómetro que varía')
plt.ylabel('Corriente (mA)')
plt.xlabel('Tiempo (s)')
plt.show()

# Gráfica de Voltaje v

ds = pd.read_csv('https://raw.githubusercontent.com/jjavierf64/Proyectos_Instrumentacion/main/S03/datosVol01.csv')

print(ds.tail())

ds = ds.set_index('t')

plt.plot(ds.v)
plt.title('Medida de la tensión en un potenciómetro que varía')
plt.ylabel('Voltaje (V)')
plt.xlabel('Tiempo (s)')
plt.show()

# Ambos Datos

dsv = pd.read_csv('https://raw.githubusercontent.com/jjavierf64/Proyectos_Instrumentacion/main/S03/datosVol01.csv')
dsc = pd.read_csv('https://raw.githubusercontent.com/jjavierf64/Proyectos_Instrumentacion/main/S03/datosCor01.csv')

dsv = dsv.set_index('t')
dsc = dsc.set_index('t')

plt.plot(dsv.v)
plt.plot(dsc.c)
plt.title('Medida de la tensión y corriente en un potenciómetro que varía')
plt.ylabel('Magnitud')
plt.xlabel('Tiempo (s)')
plt.legend(['Voltaje (V)','Corriente (mA)'],loc='upper left')
plt.show()