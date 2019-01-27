#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 316513979, Diego Armando Santillán Arriaga, Taller de Herramientas Computacionales
# Este programa recibe un laberinto en forma de una lista de listas en la que
# cada lista representa un cuadrado de una cuadrícula; si la lista contiene el valor
# true entonces no es transitable pero si contiene el valor false, sí lo es. El programa
# encuentra y devuelve la salida del laberinto.

# No pude completar el programa.

import Problema5

print'''Este programa recibe un laberinto en forma de una lista de listas en la
que cada lista representa un cuadrado de una cuadrícula; si la lista contiene el
valor true entonces no es transitable pero si contiene el valor false, sí lo es.
Ejemplo:
L=[[True, True, True, True],
   [False, False, False, True],
   [True, True, False, True]]   '''
L=input ('Introduce un laberinto según las indicaciones dadas: ')
e=input (''''ahora introduce una lista en donde indiques dónde está la entrada del
         laberinto (las filas se numeran desde el 0, comenzando desde arriba y
         contando hacia abajo y las columnas de izquierda a derecha comenzando
         desde el 0:''')
print 'La salida del laberinto es:'
print Problema5.resolver(L, e)
         
