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



#SET 1

# Gráfica Resistencia

ds = pd.read_csv('https://raw.githubusercontent.com/jjavierf64/Proyectos_Instrumentacion/main/S11/datos_1.csv')

print(ds.tail())

ds = ds.set_index('ts')

plt.plot(ds.ro)
plt.title('Medida del valor de la resistencia del termoresistor. (Primer Set)')
plt.ylabel('Resitencia (Ohms)')
plt.xlabel('Tiempo (s)')
plt.show()

# Gráfica de Temperatura

plt.plot(ds.tk)
plt.title('Medida de la temperatura definida por el termoresistor. (Primer Set)')
plt.ylabel('Temperatura (K)')
plt.xlabel('Tiempo (s)')
plt.show()




#SET 2

# Gráfica Resistencia

ds = pd.read_csv('https://raw.githubusercontent.com/jjavierf64/Proyectos_Instrumentacion/main/S11/datos_2.csv')

print(ds.tail())

ds = ds.set_index('ts')

plt.plot(ds.ro)
plt.title('Medida del valor de la resistencia del termoresistor. (Segundo Set)')
plt.ylabel('Resitencia (Ohms)')
plt.xlabel('Tiempo (s)')
plt.show()

# Gráfica de Temperatura

plt.plot(ds.tk)
plt.title('Medida de la temperatura definida por el termoresistor. (Segundo Set)')
plt.ylabel('Temperatura (K)')
plt.xlabel('Tiempo (s)')
plt.show()




#SET 3

# Gráfica Resistencia

ds = pd.read_csv('https://raw.githubusercontent.com/jjavierf64/Proyectos_Instrumentacion/main/S11/datos_3.csv')

print(ds.tail())

ds = ds.set_index('ts')

plt.plot(ds.ro)
plt.title('Medida del valor de la resistencia del termoresistor. (Tercer Set)')
plt.ylabel('Resitencia (Ohms)')
plt.xlabel('Tiempo (s)')
plt.show()

# Gráfica de Temperatura

plt.plot(ds.tk)
plt.title('Medida de la temperatura definida por el termoresistor. (Tercer Set)')
plt.ylabel('Temperatura (K)')
plt.xlabel('Tiempo (s)')
plt.show()